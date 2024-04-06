# -*- coding: UTF-8 -*-
# A part of the EnhancedDictionaries addon for NVDA
# Copyright (C) 2020 Marlon Sousa
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

import config
from logHandler import log
import speechDictHandler
from speechDictHandler import dictFormatUpgrade, dictionaries
import os


# we need to inject these methods in speechDictHandler.SpeechDict class
# they will be used to sync with other dictionaries and to create new dictionaries
# and will be called inside the dictionary dialog
def patchSpeechDict():
	speechDictHandler.SpeechDict.create = create
	speechDictHandler.SpeechDict.syncFrom = syncFrom


def create(self, fileName):
	if os.path.exists(fileName):
		raise f"can not create dictionary backed by file {fileName}"
	self.fileName = fileName
	log.debug("creating dictionary with file '%s'." % fileName)


def syncFrom(self, source):
	for entry in source:
		if not next((x for x in self if x.pattern == entry.pattern), None):
			self.append(entry)


# the functions below would be inserted right in speechDictHandler module
# as they are specific for this addon, we don't need to inject them.
# We will ratter use them right from this module
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
	dic = speechDictHandler.SpeechDict()
	dic.create(os.path.join(getProfileVoiceDictsPath(), synth.name, dictionaryFilename))
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
	dic = speechDictHandler.SpeechDict()
	dic.create(os.path.join(dictFormatUpgrade.speechDictsPath, profile.name, f"{type}.dic"))
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
		dictionaries["default"].load(os.path.join(dictFormatUpgrade.speechDictsPath, "default.dic"))
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
		fileName = os.path.join(dictFormatUpgrade.voiceDictsPath, synth.name, dictionaryFileName)
		dictionaries["voice"].load(fileName)


def _getVoiceDictionaryFileName(synth):
	try:
		dictFormatUpgrade.doAnyUpgrades(synth)
	except Exception:
		log.error("error trying to upgrade dictionaries", exc_info=True)
		pass
	if synth.isSupported("voice"):
		voice = synth.availableVoices[synth.voice].displayName
		baseName = dictFormatUpgrade.createVoiceDictFileName(synth.name, voice)
	else:
		baseName = r"{synth}.dic".format(synth=synth.name)
	return baseName


def _hasDictionaryProfile(profileName, dictionaryName):
	return os.path.exists(os.path.join(dictFormatUpgrade.speechDictsPath, profileName or "", dictionaryName))


def getProfileVoiceDictsPath():
	profile = config.conf.getActiveProfile()
	return os.path.join(dictFormatUpgrade.speechDictsPath, profile.name or "", r"voiceDicts.v1")


def _hasVoiceDictionaryProfile(profileName, synthName, voiceName):
	return os.path.exists(os.path.join(getProfileVoiceDictsPath(), synthName, voiceName))


def _loadProfileDictionary(target, profileName, dictionaryName):
	target.load(os.path.join(dictFormatUpgrade.speechDictsPath, profileName or "", dictionaryName))


def _loadProfileVoiceDictionary(target, synthName, voiceName):
	target.load(os.path.join(getProfileVoiceDictsPath(), synthName, voiceName))
