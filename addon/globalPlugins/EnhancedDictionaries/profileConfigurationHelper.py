# -*- coding: UTF-8 -*-
# A part of the EnhancedDictionaries addon for NVDA
# Copyright (C) 2020 Marlon Sousa
# This file is covered by the MIT License.
# See the file LICENSE for more details.

import config
from logHandler import log

module = 'EnhancedDictionaries'
KEEP_DICTIONARY_UPDATED_CONFIGURATION_KEY = "keepUpdatedCheckbox"


def stringToBool(value):
	if isinstance(value, bool):
		return value
	return str(value) == "True"


def getSavedKeepDictionaryUpdatedCheckboxValueForProfile():
	if module not in config.conf:
		log.debug(f"{module} not found on profile's configuration file")
		return False
	if KEEP_DICTIONARY_UPDATED_CONFIGURATION_KEY not in config.conf[module]:
		log.info(f"{KEEP_DICTIONARY_UPDATED_CONFIGURATION_KEY} not found on {module}'s configuration")
		return False
	return stringToBool(config.conf[module][KEEP_DICTIONARY_UPDATED_CONFIGURATION_KEY])


def saveKeepDictionaryUpdatedCheckboxValueForProfile(value):
	# Store as a string so the in-memory value and the value re-read from disk have the same type.
	value = str(bool(value))
	if module not in config.conf:
		config.conf[module] = {}
	if KEEP_DICTIONARY_UPDATED_CONFIGURATION_KEY not in config.conf[module]:
		config.conf[module][KEEP_DICTIONARY_UPDATED_CONFIGURATION_KEY] = value
		config.conf.save()
	if config.conf[module][KEEP_DICTIONARY_UPDATED_CONFIGURATION_KEY] != value:
		config.conf[module][KEEP_DICTIONARY_UPDATED_CONFIGURATION_KEY] = value
		config.conf.save()
