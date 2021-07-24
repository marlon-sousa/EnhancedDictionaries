# -*- coding: UTF-8 -*-
#A part of the EnhancedDictionaries addon for NVDA
#Copyright (C) 2020 Marlon Sousa
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

import addonHandler
import config
from . import dictHelper
from . import guiHelper
import globalPluginHandler
import globalVars
from logHandler import log


def _handlePostConfigProfileSwitch(resetSpeechIfNeeded=True):
	log.debug("changing profile")
	dictHelper.reloadDictionaries()


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

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self.injectProcessing()
	
	# the method below is responsible for modifying NVDA behavior.
	# we need that certain parts of NVDA behave differently than the original to insert our functionality
	# for example, dictionaries menus need to activate our enhanced dictionary dialog and
	# the classes handling the dictionary rules also need to be nodified to make more than they do.
	# we also need to register ourselves to be notified whenever the active profile changes, so we can load the specific dictionaries.
	def injectProcessing(self):
		# add utility method to ConfigManager class to allow us to get the active profile in a giher level
		config.ConfigManager.getActiveProfile = getActiveProfile
		# subscribe ourselves to be notified when the active profile changes
		config.post_configProfileSwitch.register(_handlePostConfigProfileSwitch)
		# add methods to SpeechDict class
		dictHelper.patchSpeechDict()
		# redirect menus to show the enhanced dictionaries dialog
		self.patchMenus()

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

	def onVoiceDictionaryCommand(self,evt):
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
