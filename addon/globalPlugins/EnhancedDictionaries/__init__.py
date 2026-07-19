# -*- coding: UTF-8 -*-
# A part of the EnhancedDictionaries addon for NVDA
# Copyright (C) 2020 Marlon Sousa
# This file is covered by the MIT License.
# See the file LICENSE for more details.

import addonHandler
import config
from . import dictHelper
from . import guiHelper
import globalPluginHandler
import globalVars
import gui
from logHandler import log
import speechDictHandler


def getActiveProfile(self):
	if globalVars.appArgs.secure:
		log.debug("safe profile")
		return
	log.debug(f"will return {self.profiles[-1].name}")
	return self.profiles[-1]


# for detailed explanations, see guiHelper.py file
__ = _

addonHandler.initTranslation()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	_DICT_COMMANDS = (
		"onDefaultDictionaryCommand",
		"onVoiceDictionaryCommand",
	)

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self._originalMainFrameDictionaryCommands = {}
		if globalVars.appArgs.secure:
			log.info("EnhancedDictionaries addon will not activate on secure screens")
			return
		self.injectProcessing()

	# the method below is responsible for modifying NVDA behavior.
	# we need that certain parts of NVDA behave differently than the original to insert our functionality
	# for example, dictionaries menus need to activate our enhanced dictionary dialog and
	# the classes handling the dictionary rules also need to be nodified to make more than they do.
	# we also need to react whenever something that affects the effective dictionaries changes
	# (profile switch, voice/synth change, dialog OK), so we can rebuild the in memory overlay.
	def injectProcessing(self):
		# add utility method to ConfigManager class to allow us to get the active profile in a giher level
		config.ConfigManager.getActiveProfile = getActiveProfile
		# add methods to SpeechDict class
		dictHelper.patchSpeechDict()
		# register the single reactor that rebuilds the memory source dictionaries.
		# extensionPoints keeps only weak references, so we hold strong ones for every
		# callable we register, to keep them alive for the lifetime of the addon.
		self._rebuildMemorySources = dictHelper.rebuildMemorySources
		dictHelper.dictionariesChanged.register(self._rebuildMemorySources)
		# fire the refresh hub whenever the active profile changes
		config.post_configProfileSwitch.register(self._onProfileSwitch)
		# wrap NVDA's loadVoiceDict, the single choke point through which the voice
		# dictionary is reloaded (synth change, voice change, settings ring, speech
		# settings dialog, ...). After NVDA reloads the global voice dict we fire the hub
		# so the reactor reapplies the profile voice overlay on top of it.
		self._originalLoadVoiceDict = speechDictHandler.loadVoiceDict
		speechDictHandler.loadVoiceDict = self._loadVoiceDictAndRebuild
		# redirect both dictionary gestures and menus to the enhanced dictionaries dialog
		self._patchMainFrameDictionaryCommands()
		self.patchMenus()
		# build the initial overlay for the currently active profile
		dictHelper.dictionariesChanged.notify()

	def terminate(self):
		if not globalVars.appArgs.secure:
			try:
				self._restoreMainFrameDictionaryCommands()
				speechDictHandler.loadVoiceDict = self._originalLoadVoiceDict
				config.post_configProfileSwitch.unregister(self._onProfileSwitch)
				dictHelper.dictionariesChanged.unregister(self._rebuildMemorySources)
			except Exception:
				log.error("error while unregistering EnhancedDictionaries reactors", exc_info=True)
		super(GlobalPlugin, self).terminate()

	def _onProfileSwitch(self, *args, **kwargs):
		log.debug("changing profile")
		dictHelper.dictionariesChanged.notify()

	def _loadVoiceDictAndRebuild(self, synth):
		# let NVDA reload the global voice dictionary into the definition, then fire the
		# hub so the reactor reapplies the profile voice overlay. The synth is passed
		# through because NVDA calls this while the synth is still being instantiated,
		# when synthDriverHandler.getSynth() would not yet return it.
		self._originalLoadVoiceDict(synth)
		dictHelper.dictionariesChanged.notify(synth=synth)

	def _patchMainFrameDictionaryCommands(self):
		for name in self._DICT_COMMANDS:
			self._originalMainFrameDictionaryCommands[name] = getattr(gui.mainFrame, name)
			setattr(gui.mainFrame, name, getattr(self, name))

	def _restoreMainFrameDictionaryCommands(self):
		for name, original in self._originalMainFrameDictionaryCommands.items():
			setattr(gui.mainFrame, name, original)
		self._originalMainFrameDictionaryCommands.clear()

	def patchMenus(self):
		standardDictionaryMenu = guiHelper.getDefaultDictionaryMenu()
		voiceDictionaryMenu = guiHelper.getVoiceDictionaryMenu()
		guiHelper.rebindMenu(standardDictionaryMenu, self.onDefaultDictionaryCommand)
		guiHelper.rebindMenu(voiceDictionaryMenu, self.onVoiceDictionaryCommand)

	def onDefaultDictionaryCommand(self, evt):
		# linting is complaining about from .settingsDialogs import * names
		# too risky to change it all, so we will specify what we want on a method based aproach
		dic = dictHelper.getDictionary("default")
		guiHelper.showEnhancedDictionaryDialog(dic)

	def onVoiceDictionaryCommand(self, evt):
		from synthDriverHandler import getSynth
		synth = getSynth()
		if synth.isSupported("voice"):
			voiceName = f"{synth.name}-{synth.availableVoices[synth.voice].displayName}"
		else:
			voiceName = synth.name
		# linting is complaining about from .settingsDialogs import * names
		# too risky to change it all, so we will specify what we want on a method based aproach
		dic = dictHelper.getDictionary("voice")
		# Translators: Title for voice dictionary for the current voice such as current eSpeak variant.
		guiHelper.showEnhancedDictionaryDialog(dic, __("Voice dictionary (%s)") % voiceName)
