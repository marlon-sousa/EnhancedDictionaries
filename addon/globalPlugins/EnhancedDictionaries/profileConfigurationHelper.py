import config
from logHandler import log

module = 'EnhancedDictionaries'
key = "keepUpdatedCheckbox"


def stringToBool(value):
	if value == "True":
		return True
	return False


def getSavedKeepDictionaryUpdatedCheckboxValueForProfile():
	if module not in config.conf:
		log.debug(f"{module} not found on profile's configuration file")
		return False
	if KEEP_DICTIONARY_UPDATED_CONFIGURATION_KEY not in config.conf[module]:
		log.info(f"{KEEP_DICTIONARY_UPDATED_CONFIGURATION_KEY} not found on {module}'s configuration")
		return False
	return stringToBool(config.conf[module][KEEP_DICTIONARY_UPDATED_CONFIGURATION_KEY])


def saveKeepDictionaryUpdatedCheckboxValueForProfile(value):
	if module not in config.conf:
		config.conf[module] = {}
	if KEEP_DICTIONARY_UPDATED_CONFIGURATION_KEY not in config.conf[module]:
		config.conf[module][KEEP_DICTIONARY_UPDATED_CONFIGURATION_KEY] = value
		```
		config.conf.save()
	if config.conf[module][KEEP_DICTIONARY_UPDATED_CONFIGURATION_KEY] != value:
		config.conf[module][KEEP_DICTIONARY_UPDATED_CONFIGURATION_KEY] = value
		config.conf.save()
