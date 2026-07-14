# -*- coding: UTF-8 -*-
# A part of the EnhancedDictionaries addon for NVDA
# Copyright (C) 2020 Marlon Sousa
# This file is covered by the MIT License.
# See the file LICENSE for more details.

import addonHandler
import config
from . import dictHelper
from logHandler import log
from . import profileConfigurationHelper
import gui
from gui import guiHelper
from speechDictHandler import SpeechDict
import wx

# this addon mostly complements NVDA functionalities.
# however, because the way NVDA works, when you use
# addon translation infrastructure by calling addonHandler.initTranslation() you loose access to the
# NVDA translated strings
# It is all or nothing:
# if you call addonHandler.initTranslation() the _(str) function looks for translations
# only in the addon localization files.
# if you don't, then the _(str) function looks for translations in the NVDA localization files,
# but not in the addon localization files
# In this addon, we add new buttons to specific dialogs.
# Of course the translations for these elements are not available in nvda localization files.
# In the other hand, we use the label of dictionaries (default and voice) menus to find them in the menu tree,
# in order to redirect their activation handlers to our custom dictionary dialogs.
# These menu labels are translated if NVDA is running in languages other than english.
# So now we need to access the nvda localization files to determine the menu labels,
# but we also need to access addon translation files to translate custom dialogs
# Here is what we did:
# we saved the nvda translator to the __ variable while _ variable now is used to translate addon strings


__ = _
addonHandler.initTranslation()


# we need to redirect some menus to trigger our specific dictionary dialog instead of NVDA one
# This is needed because aparently wx stores the address of the methods bound to menus activation,
# so patching the class is not enough, we need to bind the menus again
# NVDA menus are created with id WX_ANY, so it is not possible to rely on menu ids when retrieving them
# because of that, we had some options:
# - getting menus based on their position, risky because if NVDA ever changes menu positioning,
# the addon will break
# - getting menus by their label. This is saffer, but harder, cinse menu labels are localized to
# the language nvda is using
# Here is what we did:
# We searched for the current string equivalent to the original menu label,
# using the exact same translation routin NVDA uses to translate it.
def findMenuItem(menu, name):
	log.debug(f"Searching for {name}")
	return menu.FindItemById(menu.FindItem(name))


def getDictionariesMenu():
	preferencesMenu = gui.mainFrame.sysTrayIcon.preferencesMenu
	dictionaryMenu = findMenuItem(preferencesMenu, __("Speech &dictionaries"))
	if not dictionaryMenu:
		return None
	return dictionaryMenu.GetSubMenu()


def getDefaultDictionaryMenu():
	dictionariesMenu = getDictionariesMenu()
	if not dictionariesMenu:
		return None
	return findMenuItem(dictionariesMenu, __("&Default dictionary..."))


def getVoiceDictionaryMenu():
	dictionariesMenu = getDictionariesMenu()
	if not dictionariesMenu:
		return None
	return findMenuItem(dictionariesMenu, __("&Voice dictionary..."))


def rebindMenu(menu, handler):
	gui.mainFrame.sysTrayIcon.Unbind(wx.EVT_MENU, menu)
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, handler, menu)


def showEnhancedDictionaryDialog(dic, title=None):
	gui.mainFrame.popupSettingsDialog(EnhancedDictionaryDialog, title or __("Default dictionary"), dic)


# This is our new dictionary dialog.
# it presents the following changes compared to the original dialog:
# - the title of the dialog contains the profile this dictionary belongs to
# for dictionaries belonging to specific profiles, a button
# to import entries from the default profile dictionary is presented
# if a dictionary is being created (it does not exist on disc) it is activated imediately
# after the dialog closes
class EnhancedDictionaryDialog(gui.speechDict.DictionaryDialog):
	keepUpdatedCheckBox = False

	def __init__(self, parent, title, speechDict):
		self._profile = config.conf.getActiveProfile()
		title = self._makeTitle(title)
		super().__init__(parent, title, speechDict)

	def _makeTitle(self, title):
		# Translators: The profile name for normal configuration
		profileName = self._profile.name or __("normal configuration")
		return f"{title} - {profileName}"

	def makeSettings(self, settingsSizer):
		sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: The label for the filter field in the dictionary dialog.
		searchLabelText = __("Filter b&y:")
		self.searchEdit = sHelper.addLabeledControl(
			searchLabelText,
			wx.TextCtrl
		)
		self.searchEdit.Bind(wx.EVT_TEXT, self.onSearch)
		# Translators: The label for the list box of dictionary entries in speech dictionary dialog.
		entriesLabelText = __("&Dictionary entries")
		self.dictList = sHelper.addLabeledControl(
			entriesLabelText,
			wx.ListCtrl, style=wx.LC_REPORT | wx.LC_SINGLE_SEL
		)
		# Translators: The label for a column in dictionary entries list used to identify comments for the entry.
		self.dictList.InsertColumn(0, __("Comment"), width=150)
		# Translators: The label for a column in dictionary entries list used to identify pattern
		# (original word or a pattern).
		self.dictList.InsertColumn(1, __("Pattern"), width=150)
		# Translators: The label for a column in dictionary entries list and in a list of symbols
		# from symbol pronunciation dialog used to identify replacement for a pattern or a symbol
		self.dictList.InsertColumn(2, __("Replacement"), width=150)
		# Translators: The label for a column in dictionary entries list used to identify
		# whether the entry is case sensitive or not.
		self.dictList.InsertColumn(3, __("case"), width=50)
		# Translators: The label for a column in dictionary entries list used to identify
		# whether the entry is a regular expression, matches whole words, or matches anywhere.
		self.dictList.InsertColumn(4, __("Type"), width=50)
		self.offOn = (__("off"), __("on"))
		self._refreshDictList()
		self.editingIndex = -1

		bHelper = guiHelper.ButtonHelper(orientation=wx.HORIZONTAL)
		bHelper.addButton(
			parent=self,
			# Translators: The label for a button in speech dictionaries dialog to add new entries.
			label=__("&Add")
		).Bind(wx.EVT_BUTTON, self.onAddClick)

		bHelper.addButton(
			parent=self,
			# Translators: The label for a button in speech dictionaries dialog to edit existing entries.
			label=__("&Edit")
		).Bind(wx.EVT_BUTTON, self.onEditClick)

		bHelper.addButton(
			parent=self,
			# Translators: The label for a button in speech dictionaries dialog to remove existing entries.
			label=__("&Remove")
		).Bind(wx.EVT_BUTTON, self.onRemoveClick)

		bHelper.sizer.AddStretchSpacer()

		bHelper.addButton(
			parent=self,
			# Translators: The label for a button on the Speech Dictionary dialog.
			label=__("Remove all")
		).Bind(wx.EVT_BUTTON, self.onRemoveAll)

		# name of the default profile is always set to None on NVDA
		if self._profile.name:
			bHelper.addButton(
				parent=self,
				# Translators: The label for the import entries from default profile dictionary
				label=_("&import entries from default profile dictionary")
			).Bind(wx.EVT_BUTTON, self.onImportEntriesClick)

			sHelper.addItem(bHelper)

			profile = config.conf.getActiveProfile()
			if profile.name:
				self.keepUpdatedCheckBox = wx.CheckBox(
					# Translators: The name of the "keep the profile dictionary in sync" checkbox
					self, label=_("&Sync entries with default profile dictionary")
				)
				savedKeepDictionaryUpdatedCheckboxValue = (
					profileConfigurationHelper.getSavedKeepDictionaryUpdatedCheckboxValueForProfile()
				)
				self.keepUpdatedCheckBox.SetValue(savedKeepDictionaryUpdatedCheckboxValue)
				sHelper.addItem(self.keepUpdatedCheckBox)

	def _getFilterText(self):
		searchEdit = getattr(self, "searchEdit", None)
		if searchEdit is None:
			return ""
		return searchEdit.GetValue()

	def _entryMatchesFilter(self, entry, filterText):
		if not filterText:
			return True
		return any(
			filterText in (value or "").lower()
			for value in (entry.comment, entry.pattern, entry.replacement)
		)

	def _refreshDictList(self, selectedEntryIndex=None):
		"""Rebuild the visible entry list and preserve its mapping to the full dictionary."""
		filterText = self._getFilterText().lower()
		self.dictList.DeleteAllItems()
		selectedRow = -1

		for entryIndex, entry in enumerate(self.tempSpeechDict):
			if not self._entryMatchesFilter(entry, filterText):
				continue
			row = self.dictList.Append((
				entry.comment,
				entry.pattern,
				entry.replacement,
				self.offOn[int(entry.caseSensitive)],
				EnhancedDictionaryDialog.TYPE_LABELS[entry.type]
			))
			self.dictList.SetItemData(row, entryIndex)
			if entryIndex == selectedEntryIndex:
				selectedRow = row

		if selectedRow >= 0:
			self.dictList.Select(selectedRow)
			self.dictList.Focus(selectedRow)

	def onSearch(self, evt):
		self._refreshDictList()
		evt.Skip()

	def _getSelectedEntryIndex(self):
		"""Return the selected visible row and its backing dictionary entry index."""
		if self.dictList.GetSelectedItemCount() != 1:
			return (-1, -1)
		rowIndex = self.dictList.GetFirstSelected()
		if rowIndex < 0:
			return (-1, -1)
		try:
			entryIndex = self.dictList.GetItemData(rowIndex)
		except (RuntimeError, TypeError):
			log.debugWarning(
				"Could not retrieve dictionary entry index from the selected row",
				exc_info=True
			)
			return (-1, -1)
		if not isinstance(entryIndex, int) or not 0 <= entryIndex < len(self.tempSpeechDict):
			log.debugWarning(f"Ignoring invalid dictionary entry index: {entryIndex!r}")
			return (-1, -1)
		return (rowIndex, entryIndex)

	def onAddClick(self, evt):
		entryCountBefore = len(self.tempSpeechDict)
		super().onAddClick(evt)
		if len(self.tempSpeechDict) == entryCountBefore:
			return
		addedEntryIndex = len(self.tempSpeechDict) - 1
		self._refreshDictList(selectedEntryIndex=addedEntryIndex)
		self.dictList.SetFocus()

	def onEditClick(self, evt):
		rowIndex, entryIndex = self._getSelectedEntryIndex()
		if entryIndex < 0:
			return
		entry = self.tempSpeechDict[entryIndex]
		entryDialog = gui.speechDict.DictionaryEntryDialog(self)
		entryDialog.patternTextCtrl.SetValue(entry.pattern)
		entryDialog.replacementTextCtrl.SetValue(entry.replacement)
		entryDialog.commentTextCtrl.SetValue(entry.comment)
		entryDialog.caseSensitiveCheckBox.SetValue(entry.caseSensitive)
		entryDialog.setType(entry.type)
		if entryDialog.ShowModal() == wx.ID_OK:
			self.tempSpeechDict[entryIndex] = entryDialog.dictEntry
			self._refreshDictList(selectedEntryIndex=entryIndex)
			self.dictList.SetFocus()
		entryDialog.Destroy()

	def onRemoveClick(self, evt):
		selectedEntryIndexes = []
		rowIndex = self.dictList.GetFirstSelected()
		while rowIndex >= 0:
			try:
				entryIndex = self.dictList.GetItemData(rowIndex)
			except (RuntimeError, TypeError):
				log.debugWarning(
					"Could not retrieve dictionary entry index from a selected row",
					exc_info=True
				)
			else:
				if isinstance(entryIndex, int) and 0 <= entryIndex < len(self.tempSpeechDict):
					selectedEntryIndexes.append(entryIndex)
				else:
					log.debugWarning(f"Ignoring invalid dictionary entry index: {entryIndex!r}")
			rowIndex = self.dictList.GetNextSelected(rowIndex)

		if not selectedEntryIndexes:
			return
		for entryIndex in sorted(set(selectedEntryIndexes), reverse=True):
			del self.tempSpeechDict[entryIndex]
		self._refreshDictList()
		self.dictList.SetFocus()

	def onRemoveAll(self, evt):
		if (
			gui.messageBox(
				# Translators: A prompt for confirmation on the Speech Dictionary dialog.
				__("Are you sure you want to remove all the entries in this dictionary?"),
				# Translators: The title on a prompt for confirmation on the Speech Dictionary dialog.
				__("Remove all"),
				style=wx.YES | wx.NO | wx.NO_DEFAULT,
			)
			!= wx.YES
		):
			return
		del self.tempSpeechDict[:]
		self._refreshDictList()
		self.dictList.SetFocus()

	def onOk(self, evt):
		# super().onOk saves the edited (profile-own on named profiles, global on the
		# normal profile) dictionary to its own file. It never touches the in memory
		# overlay that NVDA processes.
		super().onOk(evt)

		if self._profile.name:
			checkboxValue = self.keepUpdatedCheckBox.GetValue()
			profileConfigurationHelper.saveKeepDictionaryUpdatedCheckboxValueForProfile(checkboxValue)

		# rebuild the memory source dictionaries so the just saved edits (and the sync
		# checkbox) take effect immediately, without waiting for the next profile switch.
		dictHelper.dictionariesChanged.notify()

	def onImportEntriesClick(self, evt):
		sourceFileName = self.speechDict.fileName.replace(f"{self._profile.name}\\", "")
		log.debug(f"Importing entries from default dictionary at {sourceFileName}")
		source = SpeechDict()
		source.load(sourceFileName)
		self.tempSpeechDict.syncFrom(source)
		self._refreshDictList()
		self.dictList.SetFocus()