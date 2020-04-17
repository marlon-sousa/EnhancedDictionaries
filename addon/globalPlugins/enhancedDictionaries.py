# -*- coding: UTF-8 -*-
#A part of the BluetoothAudio addon for NVDA
#Copyright (C) 2018 Tony Malykh
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

import addonHandler
import config
import globalPluginHandler
import globalVars
import gui
from gui import guiHelper
from logHandler import log
import speechDictHandler
from speechDictHandler.dictFormatUpgrade import speechDictsPath, createVoiceDictFileName, doAnyUpgrades, voiceDictsPath
from speechDictHandler import dictionaries
import os
import ui
import wx
import scriptHandler
from scriptHandler import script

class SpeechDict(speechDictHandler.SpeechDict):

	def __init():
		super(SpeechDict, self).__init()

	def create(self, fileName):
		if os.path.exists(fileName):
			raise f"can not create dictionary backed by file {fileName}"
		self.fileName = fileName
		log.debug("creating dictionary with file '%s'." % fileName)
	
	def syncFrom(self, source):
		for entry in source:
			if not next((x for x in self if x.pattern == entry.pattern), None):
				self.append(entry)


def _handlePostConfigProfileSwitch(resetSpeechIfNeeded=True):
	log.debug("changing profile")
	reloadDictionaries()


def reloadDictionaries():
	from synthDriverHandler import getSynth
	synth = getSynth()
	loadProfileDict()
	loadVoiceDict(synth)
	log.debug(f"loaded dictionaries for profile {config.conf.getActiveProfile().name or 'default'}")




def _getVoiceDictionary(profile):
	from synthDriverHandler import getSynth
	synth = getSynth()
	dictionaryFilename = _getVoiceDictionaryFileName(synth)
	# if we are om default profile or the specific dictionary profile is already loaded
	if not profile.name or _hasVoiceDictionaryProfile(profile.name, synth.name, dictionaryFilename):
		# we are with the correct dictionary loaded. Just return it.
		log.debug(f"Voice dictionary, backed by {dictionaries['voice'].fileName} was requested")
		return dictionaries["voice"]
	# we are on a user profile for which there is no dictionary created for the current voice.
	# The current loaded dictionary is the default profile one.
	# As we have beem called to get the profile dictionary for the current voice and it still does not exist,
	# We will create it now and pass the new, empty dictionary to the caller, but won't save it.
	# This is a task the caller should do when and if they wish
	dic = SpeechDict()
	dic.create(os.path.join(dictFormatUpgrade.getProfileVoiceDictsPath(), synth.name, dictionaryFilename))
	log.debug(
		f"voice dictionary was requested for profile {profile.name}, but the backing file does not exist."
		f" A New dictionary was created, set to be backed by {dic.fileName} if it is ever saved."
	)
	return dic


def getDictionary(type):
	profile = config.conf.getActiveProfile()
	if(type == "voice"):
		return _getVoiceDictionary(profile)
	# if we are om default profile or the specific dictionary profile is already loaded
	if not profile.name or _hasDictionaryProfile(profile.name, f"{type}.dic"):
		# we are with the correct dictionary loaded. Just return it.
		log.debug(f"{type} dictionary, backed by {dictionaries[type].fileName} was requested")
		return dictionaries[type]
	# we are on a user profile for which there is no dictionary created.
	# The current loaded dictionary is the default profile one.
	# As we have beem called to get the current profile dictionary and it still does not exist,
	# We will create it now and pass the new, empty dictionary to the caller, but won't save it.
	# This is a task the caller should do when and if they wish
	dic = SpeechDict()
	dic.create(os.path.join(speechDictsPath, profile.name, f"{type}.dic"))
	log.debug(
		f"{type} dictionary was requested for profile {profile.name}, but the backing file does not exist."
		f" A New dictionary was created, set to be backed by {dic.fileName} if it is ever saved."
	)
	return dic


def loadProfileDict():
	profile = config.conf.getActiveProfile()
	if _hasDictionaryProfile(profile.name, "default.dic"):
		_loadProfileDictionary(dictionaries["default"], profile.name, "default.dic")
	else:
		dictionaries["default"].load(os.path.join(speechDictsPath, "default.dic"))
	dictionaries["builtin"].load("builtin.dic")


def loadVoiceDict(synth):
	"""Loads appropriate dictionary for the given synthesizer.
It handles case when the synthesizer doesn't support voice setting.
"""
	dictionaryFileName = _getVoiceDictionaryFileName(synth)
	profile = config.conf.getActiveProfile()
	if(_hasVoiceDictionaryProfile(profile.name, synth.name, dictionaryFileName)):
		_loadProfileVoiceDictionary(dictionaries["voice"], synth.name, dictionaryFileName)
	else:
		fileName = os.path.join(voiceDictsPath, synth.name, dictionaryFileName)
		dictionaries["voice"].load(fileName)


def _getVoiceDictionaryFileName(synth):
	try:
		doAnyUpgrades(synth)
	except:
		log.error("error trying to upgrade dictionaries", exc_info=True)
		pass
	if synth.isSupported("voice"):
		voice = synth.availableVoices[synth.voice].displayName
		baseName = createVoiceDictFileName(synth.name, voice)
	else:
		baseName=r"{synth}.dic".format(synth=synth.name)
	return baseName


def _hasDictionaryProfile(profileName, dictionaryName):
	return os.path.exists(os.path.join(speechDictsPath, profileName or "", dictionaryName))

def getProfileVoiceDictsPath():
	profile = config.conf.getActiveProfile()
	return os.path.join(speechDictsPath, profile.name or "", r"voiceDicts.v1")


def _hasVoiceDictionaryProfile(profileName, synthName, voiceName):
	return os.path.exists(os.path.join(getProfileVoiceDictsPath(), synthName, voiceName))


def _loadProfileDictionary(target, profileName, dictionaryName):
	target.load(os.path.join(speechDictsPath, profileName or "", dictionaryName))


def _loadProfileVoiceDictionary(target, synthName, voiceName):
	target.load(os.path.join(getProfileVoiceDictsPath(), synthName, voiceName))

def getActiveProfile(self):
	if globalVars.appArgs.secure:
		return
	return self.profiles[-1]

def enhanceConfigManager(configManager):
	configManager.getActiveProfile = getActiveProfile.__get__(configManager)

class ConfigManager(config.ConfigManager):
	def __init():
		super(ConfigManager, self).__init()
	
	def getActiveProfile(self):
		if globalVars.appArgs.secure:
			log.debug("safe profile")
			return
		log.debug(f"will return {self.profiles[-1].name}")
		return self.profiles[-1]

def getActiveProfile(self):
	if globalVars.appArgs.secure:
		log.debug("safe profile")
		return
	log.debug(f"will return {self.profiles[-1].name}")
	return self.profiles[-1]

def findMenuItem(menu, name):
	log.debug(f"Searching for {name}")
	return menu.FindItemById(menu.FindItem(name))


def getDictionariesMenu():
	preferencesMenu = gui.mainFrame.sysTrayIcon.preferencesMenu
	dictionaryMenu = findMenuItem(preferencesMenu, _("Speech &dictionaries"))
	if not dictionaryMenu:
		return None
	return dictionaryMenu.GetSubMenu()

def getDefaultDictionaryMenu():
	dictionariesMenu = getDictionariesMenu()
	if not dictionariesMenu:
		return None
	return findMenuItem(dictionariesMenu, _("&Default dictionary..."))


def getVoiceDictionaryMenu():
	dictionariesMenu = getDictionariesMenu()
	if not dictionariesMenu:
		return None
	return findMenuItem(dictionariesMenu, _("&Voice dictionary..."))




class ProfileDictionaryDialog(gui.settingsDialogs.DictionaryDialog):
	
	PATTERN_COL = 1
	
	def __init__(self, parent,title,speechDict):
		self._profile = config.conf.getActiveProfile()
		title = self._makeTitle(title)
		log.debug(f"exibido {self._makeTitle(title)}")
		super(ProfileDictionaryDialog, self).__init__(parent,title,speechDict)
	
	def _makeTitle(self, title):
		# Translators: The profile name for normal configuration
		profileName = self._profile.name or _("normal configuration")
		log.debug(f"will return {title} - {profileName}")
		return f"{title} - {profileName}"
	
	def makeSettings(self, settingsSizer):
		sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: The label for the list box of dictionary entries in speech dictionary dialog.
		entriesLabelText=_("&Dictionary entries")
		self.dictList = sHelper.addLabeledControl(
			entriesLabelText,
			wx.ListCtrl, style=wx.LC_REPORT | wx.LC_SINGLE_SEL
		)
		# Translators: The label for a column in dictionary entries list used to identify comments for the entry.
		self.dictList.InsertColumn(0,_("Comment"),width=150)
		# Translators: The label for a column in dictionary entries list used to identify pattern (original word or a pattern).
		self.dictList.InsertColumn(1,_("Pattern"),width=150)
		# Translators: The label for a column in dictionary entries list and in a list of symbols from symbol pronunciation dialog used to identify replacement for a pattern or a symbol
		self.dictList.InsertColumn(2,_("Replacement"),width=150)
		# Translators: The label for a column in dictionary entries list used to identify whether the entry is case sensitive or not.
		self.dictList.InsertColumn(3,_("case"),width=50)
		# Translators: The label for a column in dictionary entries list used to identify whether the entry is a regular expression, matches whole words, or matches anywhere.
		self.dictList.InsertColumn(4,_("Type"),width=50)
		self.offOn = (_("off"),_("on"))
		for entry in self.tempSpeechDict:
			self.dictList.Append((entry.comment,entry.pattern,entry.replacement,self.offOn[int(entry.caseSensitive)],ProfileDictionaryDialog.TYPE_LABELS[entry.type]))
		self.editingIndex=-1

		bHelper = guiHelper.ButtonHelper(orientation=wx.HORIZONTAL)
		bHelper.addButton(
			parent=self,
			# Translators: The label for a button in speech dictionaries dialog to add new entries.
			label=_("&Add")
		).Bind(wx.EVT_BUTTON, self.OnAddClick)

		bHelper.addButton(
			parent=self,
			# Translators: The label for a button in speech dictionaries dialog to edit existing entries.
			label=_("&Edit")
		).Bind(wx.EVT_BUTTON, self.OnEditClick)

		bHelper.addButton(
			parent=self,
			# Translators: The label for a button in speech dictionaries dialog to remove existing entries.
			label=_("&Remove")
		).Bind(wx.EVT_BUTTON, self.OnRemoveClick)

		if(self._profile.name):
			bHelper.addButton(
				parent=self,
				# Translators: The label for the import entries from default profile dictionary
				label=_("&import entries from default profile dictionary")
			).Bind(wx.EVT_BUTTON, self.onImportEntriesClick)

		sHelper.addItem(bHelper)

	def hasEntry(self, pattern):
		for row in range(self.dictList.GetItemCount()):
			if self.dictList.GetItem(row, self.PATTERN_COL).GetText() == pattern:
				return True
		return False

	def onOk(self,evt):
		newDictionary = not os.path.exists(self.speechDict.fileName)
		super().onOk(evt)
		if newDictionary:
			# if we are saving a dictionary that didn't exist before (user just performed the first edition)
			# we have to activate it now, otherwise it will be effective only on next profile switch.
			log.debug(f"Activating new dictionary {self.speechDict.fileName}")
			reloadDictionaries()

	def onImportEntriesClick(self, evt):
		sourceFileName = self.speechDict.fileName.replace(f"{self._profile.name}\\", "")
		log.debug(f"Importing entries from default dictionary at {sourceFileName}")
		source = speechDictHandler.SpeechDict()
		source.load(sourceFileName)
		self.syncDictionaryFrom(source)
		for entry in self.tempSpeechDict:
			if not self.hasEntry(entry.pattern):
				self.dictList.Append((
					entry.comment,
					entry.pattern,
					entry.replacement,
					self.offOn[int(entry.caseSensitive)],
					ProfileDictionaryDialog.TYPE_LABELS[entry.type]
				))
		self.dictList.SetFocus()

	def syncDictionaryFrom(self, source):
		for entry in source:
			if not next((x for x in self.tempSpeechDict if x.pattern == entry.pattern), None):
				self.tempSpeechDict.append(entry)

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = _("BluetoothAudio")

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		log.debug("constructor")
		self.injectProcessing()
		config.post_configProfileSwitch.register(_handlePostConfigProfileSwitch)
	
	def injectProcessing(self):
		config.conf.getActiveProfile = getActiveProfile.__get__(config.conf)
		self.patchMenus()
		log.debug("called function round rounded round")

	def patchMenus(self):
		standardDictionaryMenu = getDefaultDictionaryMenu()
		voiceDictionaryMenu = getVoiceDictionaryMenu()
		gui.mainFrame.sysTrayIcon.Unbind(wx.EVT_MENU, standardDictionaryMenu)
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onDefaultDictionaryCommand, standardDictionaryMenu)
	
	def onDefaultDictionaryCommand(self, evt):
		# linting is complaining about from .settingsDialogs import * names
		# too risky to change it all, so we will specify what we want on a method based aproach
		log.debug("chamasticocact")
		dic = getDictionary("default")
		# Translators: Title for default speech dictionary dialog.
		gui.mainFrame._popupSettingsDialog(ProfileDictionaryDialog, _("Default dictionary"), dic)

	@script(description="Moves to parent in tree view.", gestures=['kb:NVDA+alt+a'])
	def script_moveToParent(self, gesture):
		ui.message(_("&Default dictionary..."))
    