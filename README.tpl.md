# EnhancedDictionaries ${addon_version}
Nvda ADDON for handling more advanced dictionaries processing

## download
Download the [Enhanced Dictionaries ${addon_version} addon](https://github.com/marlon-sousa/EnhancedDictionaries/releases/download/${addon_version}/EnhancedDictionaries-${addon_version}.nvda-addon)

## Features

### Profile specific dictionaries
The way NVDA applies conditional settings, such as document formatting and others, is through the use of profiles.

Profiles are groups of settings that can, together, be applied conditionally to the screen reader.

For example, you can create a profile for coding applications, in which punctuation level is set to all, indentation announcement is set to tones and speech rate is set to a slower level, so you can read code in a better way. You can, then, associate this profile with visual studio, eclipse, notepad plus plus and Visual Studio Code, so that when any of these applications become active these configurations will automatically apply.

When you alt tab to other applications, or when you close one of these applications and land in desktop, for example, the default configuration takes place. It is then possible to easily jump from your coding application to a browser and, without pressing any keys, read without punctuations in the browser and have your specific configuration applied when you are back on your code environment.

NVDA dictionaries are powerful, offering great features such as regular expression substitution. However, there is currently no way to attach dictionaries to profiles on NVDA.

This means that if you set a substitution in the default dictionary, it will be applied in all cases, even in applications or situations where you might wish they are not.

This addon implements profile context when processing and creating / editing dictionaries. 

#### How it works?

Simply install the addon. When it's active:

* Dictionaries are now correctly handled taking in consideration the active profile.
* If dictionaries (default or voice specific) exist for the current profile, they are used.
* If they don't exist, the dictionaries for default profile are used. This is consistent to the way NVDA behaves, in the sense that when I create a new profile the configurations I don't change on this new profile are taken from the default one.

    Similarly, if I don't set a dictionary for a profile, the default dictionary is used.

* Voice dictionaries behave the exact same way: if there is a voice specific dictionary for the active profile, it is used. Otherwise, the dictionary for that voice from the default profile (if it exists) is used.
* The dictionary dialog, when opened, always shows on its title what profile that dictionary relates to.
* The active profile will determine which dictionary is opened for editing when the default or voice dictionary menus are activated.

    This is consistent to the way NVDA behaves, because if one goes to settings and change a setting, this will be saved on the active profile.

    Similarly, the opened dictionary will belong to that profile.

* If a given dictionary does not exist on an active profile and the dictionary dialog is opened, a new dictionary for that profile will be created.

    It will show no entries, as it is new. However, it won't be saved until the user closes that dialog clicking on "ok".

    If they do, the new dictionary will be effective. If they cancel the dialog, the default profile dictionary will still be used and no profile specific dictionary is saved.

* When a new profile specific dictionary is created, it becomes effective and, thus, the patterns on the default dictionary are no longer active for that profile.

    This might be the desired behavior, but perhaps not. Perhaps the user wants to use all the patterns from the default dictionary plus new patterns only active on this profile.

* To cover this possibility, a new button, called "import entries from default dictionary profile", is created in the dictionary dialog.

    This button appears only when a profile specific dictionary is being edited. On activation, it behaves the following way:
    
    - The entries from default dictionary (or voice specific dictionary) from the default profile are read.
    - Entries that are not found on the dictionary being edited are added to it.
    - If an entry from the default (or voice) dictionary is found on the dictionary being edited, it does not overwrite the current entry.
    - The import does not save the new entries on disc. It just adds imported entries in the entries list in the dictionary dialog. Focus is placed on the list and the user then has the oportunity to review the new list of entries, as if they have typed by hand all of them.

*  Whenever the user creates a dictionary on a specific profile, it is effective immediately for that profile.
* Whenever a profile changes, the specific dictionaries (default and voice) become active immediately. If these dictionaries do not exist, the default profile one's are used.
* Builtin and temp dictionaries aren't affected, they are not dependent on profiles, the latter because it is temporary, the former because it is built in.

# Contributing and translating

If you want to contribute or translate this addon, please access the [project repository](https://github.com/marlon-sousa/EnhancedDictionaries) and find instructions on the contributing.md in the english documentation directory.

## Contributors

Special thanks to

* Ângelo Miguel Abrantes - Portuguese translation
* Rémy Ruiz - French translation
* Rémy Ruiz - Spanish translation
* Tarik Hadžirović - Croatian translation
*  Thiago Seus - Brazilian Portuguese translation
* Umut KORKMAZ - Turkish translation
