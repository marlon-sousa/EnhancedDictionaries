import config
from logHandler import log

module = 'EnhancedDictionaries'
key = "keepUpdatedCheckbox"


def stringToBool(value):
	if value == "True":
		return True
	return False


def getSavedCheckboxValueForProfile():
	if module not in config.conf:
		log.info("o módulo não foi encontrado na configuração")
		return False
	if key not in config.conf[module]:
		log.info("a chave não foi encontrada no módulo.")
		return False
	return stringToBool(config.conf[module][key])


def saveCheckboxValueForProfile(value):
	if module not in config.conf:
		config.conf[module] = {}
	if key not in config.conf[module]:
		config.conf[module][key] = value
		config.conf.save()
	if config.conf[module][key] != value:
		config.conf[module][key] = value
		config.conf.save()
