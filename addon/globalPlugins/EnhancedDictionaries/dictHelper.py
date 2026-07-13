# -*- coding: UTF-8 -*-
# A part of the EnhancedDictionaries addon for NVDA
# Copyright (C) 2020 Marlon Sousa
# This file is covered by the MIT License.
# See the file LICENSE for more details.

import config
import extensionPoints
from NVDAState import WritePaths
from logHandler import log
import speechDictHandler
from speechDictHandler import dictFormatUpgrade, dictionaries, SpeechDict
import os
from . import profileConfigurationHelper


# Addon-owned refresh hub.
# Every trigger that could change the effective (memory source) dictionaries fires
# this action; the single registered reactor (rebuildMemorySources) does the work.
# This keeps the rebuild logic in exactly one place. See __init__.py for the wiring
# and for the strong references that keep the reactors alive (extensionPoints uses
# weak references).
dictionariesChanged = extensionPoints.Action()


# we inject this method in speechDictHandler.SpeechDict so a dictionary can be
# augmented with the entries of another one (patterns already present are kept).
# It is used both when building the overlay memory source and by the "import entries
# from default profile dictionary" button in the dialog.
def patchSpeechDict():
	speechDictHandler.SpeechDict.syncFrom = syncFrom


def syncFrom(self, source):
	for entry in source:
		if not next((x for x in self if x.pattern == entry.pattern), None):
			self.append(entry)


def _keepDictionaryUpdated():
	return profileConfigurationHelper.getSavedKeepDictionaryUpdatedCheckboxValueForProfile()


# ---------------------------------------------------------------------------
# Memory sources (what NVDA actually processes).
#
# NVDA processes speechDictHandler.dictionaries[type] for each type in dictTypes
# (see speechDictHandler.processText). Those objects are our memory sources. We never
# write them to disk; we rebuild their contents in place on every relevant trigger so:
# - Normal profile              -> global entries only (plain NVDA behaviour).
# - Named profile, sync off     -> profile-own entries only (isolated).
# - Named profile, sync on      -> profile-own first, then global entries whose pattern
#                                  is not already present (profile wins), applied in
#                                  NVDA's single sub pass for that dictionary.
# Base and global entries are loaded fresh from disk on each rebuild, so a new entry in
# the main dictionary is picked up live by every synced profile with zero duplication.
# ---------------------------------------------------------------------------
def rebuildMemorySources(synth=None):
	profileName = config.conf.getActiveProfile().name
	_rebuildDefaultMemorySource()
	_rebuildVoiceMemorySource(synth)
	log.debug(f"Rebuilt memory source dictionaries for profile {profileName or 'normal configuration'}")


def _rebuildDefaultMemorySource():
	profile = config.conf.getActiveProfile()
	memorySource = dictionaries["default"]
	globalFileName = WritePaths.speechDictDefaultFile
	if not profile.name:
		# Normal profile: the memory source is the global default dictionary.
		memorySource.load(globalFileName)
		return
	# Named profile: profile-own entries, optionally overlaid with the global ones.
	# load() clears the dictionary (leaving it empty when the file is missing) and sets
	# fileName; we never save this object, so pointing it at the profile file is only for
	# coherence.
	profileFileName = os.path.join(WritePaths.speechDictsDir, profile.name, "default.dic")
	memorySource.load(profileFileName)
	if _keepDictionaryUpdated():
		globalDict = SpeechDict()
		globalDict.load(globalFileName)
		memorySource.syncFrom(globalDict)


def _rebuildVoiceMemorySource(synth=None):
	# When the rebuild is triggered by NVDA reloading the voice dictionary, the synth is
	# passed explicitly: at that moment synthDriverHandler._curSynth may not be set yet
	# (the synth is still being instantiated), so getSynth() would return None. For the
	# other triggers (profile switch, dialog OK) we look the active synth up ourselves.
	if synth is None:
		from synthDriverHandler import getSynth
		synth = getSynth()
	if synth is None:
		return
	profile = config.conf.getActiveProfile()
	memorySource = dictionaries["voice"]
	baseName = _getVoiceDictionaryFileName(synth)
	globalFileName = os.path.join(WritePaths.voiceDictsDir, synth.name, baseName)
	if not profile.name:
		# Normal profile: the memory source is the global voice dictionary. NVDA reloads
		# this itself on synth/voice change (loadVoiceDict) before we run, so we simply
		# keep it in sync here.
		memorySource.load(globalFileName)
		return
	profileFileName = os.path.join(getProfileVoiceDictsPath(), synth.name, baseName)
	memorySource.load(profileFileName)
	if _keepDictionaryUpdated():
		globalDict = SpeechDict()
		globalDict.load(globalFileName)
		memorySource.syncFrom(globalDict)


# ---------------------------------------------------------------------------
# Editable dictionaries (what the dialog shows and saves).
#
# On the normal profile this is the global dictionary itself (editing it is normal NVDA
# behaviour), which is also the memory source. On a named profile it is a separate
# SpeechDict backed by the profile-own .dic file (empty if the file does not exist yet);
# saving it and firing dictionariesChanged rebuilds the memory source.
# ---------------------------------------------------------------------------
def getDictionary(type):
	profile = config.conf.getActiveProfile()
	if type == "voice":
		return _getEditableVoiceDictionary(profile)
	return _getEditableDefaultDictionary(profile)


def _getEditableDefaultDictionary(profile):
	if not profile.name:
		# Normal profile: edit the global (memory source) dictionary directly.
		log.debug(f"Default dictionary, backed by {dictionaries['default'].fileName} was requested")
		return dictionaries["default"]
	profileFileName = os.path.join(WritePaths.speechDictsDir, profile.name, "default.dic")
	return _loadEditableDictionary(profileFileName)


def _getEditableVoiceDictionary(profile):
	from synthDriverHandler import getSynth
	synth = getSynth()
	if not profile.name:
		# Normal profile: edit the global (memory source) voice dictionary directly.
		log.debug(f"Voice dictionary, backed by {dictionaries['voice'].fileName} was requested")
		return dictionaries["voice"]
	baseName = _getVoiceDictionaryFileName(synth)
	profileFileName = os.path.join(getProfileVoiceDictsPath(), synth.name, baseName)
	return _loadEditableDictionary(profileFileName)


def _loadEditableDictionary(fileName):
	# Return the profile-own dictionary, loading it if the file exists.
	# When the file does not exist yet we hand back an empty dictionary that already
	# knows where it will be saved, so the first edition creates the file on dialog OK.
	dic = SpeechDict()
	if os.path.exists(fileName):
		dic.load(fileName)
		log.debug(f"profile dictionary backed by {fileName} was requested")
	else:
		dic.fileName = fileName
		log.debug(
			f"profile dictionary was requested, but the backing file {fileName} does not exist."
			" A new empty dictionary was created, to be saved there if it is ever edited."
		)
	return dic


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


def getProfileVoiceDictsPath():
	profile = config.conf.getActiveProfile()
	return os.path.join(WritePaths.speechDictsDir, profile.name or "", r"voiceDicts.v1")
