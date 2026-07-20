# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries
from site_scons.site_tools.NVDATool.utils import _


addon_info = AddonInfo(
    addon_name="EnhancedDictionaries",
    # Translators: Summary/title for this add-on.
    addon_summary=_("Enhanced dictionaries processing for NVDA"),
    # Translators: Long description for this add-on in add-on store.
    addon_description=_("""This addon introduces better dictionaries handling for NVDA.
It is now possible to use profile specific dictionaries, which eenables better productivity by allowing you to use different dictionaries for different applications and scenarius."""),
    # Translators: what's new text for this add-on version shown in add-on store.
    addon_changelog=_("""Version 1.7.1:
* Dictionary keyboard gestures for the default and voice dictionaries now open the enhanced dictionaries dialog, matching the behavior of the dictionary menus.

Version 1.7.0:
* Compatible with NVDA 2026.1, which is now the minimum supported version.
* The "Sync entries with default profile dictionary" option now works as a live overlay applied while speech is processed, instead of copying entries into the profile dictionary. The default profile entries take effect for the synced profile without ever being written to its dictionary file, so they no longer appear in the entries list, changes made to the default dictionary are picked up automatically by every synced profile, and your profile specific entries always take priority.
* The synced overlay is now reapplied automatically whenever the voice or the synthesizer changes, including through the settings ring and the Speech settings dialog, so voice specific dictionaries stay correct.
* Fixed the "Sync entries with default profile dictionary" checkbox not remembering its state when the dictionary dialog was reopened.
* Documented the sync option in the readme in English and in all translations, and made its checkbox label translatable.
* Modernized the add-on build system and project tooling."""),
    addon_version="1.7.1",
    addon_author="Marlon Brandão de Sousa <marlon.bsousa@gmail.com>",
    addon_url="https://github.com/marlon-sousa/EnhancedDictionaries",
    addon_sourceURL="https://github.com/marlon-sousa/EnhancedDictionaries",
    addon_docFileName="readme.html",
    addon_minimumNVDAVersion="2026.1",
    addon_lastTestedNVDAVersion="2026.1.0",
    addon_updateChannel=None,
    addon_license="Mit License",
    addon_licenseURL="https://github.com/marlon-sousa/EnhancedDictionaries/blob/master/LICENSE",
)


pythonSources: list[str] = ["addon/globalPlugins/EnhancedDictionaries/*.py"]
i18nSources: list[str] = pythonSources + ["buildVars.py"]

# Paths are relative to the addon directory when building the bundle.
excludedFiles: list[str] = [
    "doc/*/contributing*.*",
    "doc/*/*.tpl.md",
]

baseLanguage: str = "en"
markdownExtensions: list[str] = []

brailleTables: BrailleTables = {}
symbolDictionaries: SymbolDictionaries = {}
