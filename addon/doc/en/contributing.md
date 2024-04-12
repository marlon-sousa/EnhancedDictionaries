# Contributing


## building the addon


### Local environment

Although not mandatory, we suggest you perform the following:

1. Clone NVDA in a folder at the same level as this project.  
For example, if this project is cloned at c:\projects\EnhancedDictionaries, NVDA should be cloned at c:\projects\nvda.  
Perform a clone with the --recursive flag. If NVDA is already cloned, make sure it is up to date, fetching and then synchronizing the master branch with the NVDA upstream master branch.  
Perform a git submodule update --init command to make sure git submodules are correctly synchronized.
2. Perform a git checkout in the release-2024.1 tag in the NVDA project. You don't need to build NVDA, just having the source code at the release branch is enough.
3. Install visual studio code, if it is not installed. Although you can use other environments, the optimal setup requires visual studio code.
4. Open the EnhancedDictionaries folder in VS Code. From command line, perform the "code ." command, or use the file / open folder menus on visual studio code itself and select the folder where this project is cloned.
5. Use ctrl + shift + x to access the extensions widget in Visual studio code. Tab umtil the recomended section and install the recomended extensions.
6. Restart visual studio code.
7. Now, whenever you are navigating through code, pressing f12 in a NVDA object should take you to its source in NVDA project.

### Dependencies

You will need:

* python 3.11.
* pip must be configured
* scons (pip install scons)
* markdown (pip install markdown)
* msgfmt utility. The easiest way of getting it is by installing git bash and choosing to include bash tools at command prompt


#### Pre-commit

It is strongly recomended that you install pre-commit.

* pip imstall pre-commit
* pre-commit install

This will imstall pre-commit and configure its hooks, so that whenever you perform a commit several checks will apply.  
Should any of them fail, the commit will not be allowed.
This helps to ensure your commits have quality. You can bypass the check, however be aware that a pull request check will also apply these same checks and merge will be disabled should any of them fail, even if someone approves the pull request.

You can trigger the pre-commit checks at any time without performing a commit by issuing "pre-commit run --all-files".

#### Flake8

One of the pre-commit hooks is flake8, a python linter which, ammong other things, help to make sure the project has a consistent formating and that good practices are in place.

Visual Studio code recomended extensions include flake8, so that you can be warned while editing code when something needs to be fixed.

The visual studio code extension and the pre-commit flake8 hooks use the same configuration.

### building

Once you have everything installed, issuing scons at the root of the project should build the addon and generate docs.

## translations

### translating the addon

Assuming you have everything set up to build the addom (see previous topic) issuing scons pot should generate a pot file at the root project directory. It is them possible to generate and contribute the .po files for your language.
Current languages can be found at /addon/locale directory

### translating documentation

Documentation translations are generated from .tpl.md (not from .md) files. This is why, except from this file (read.md) at the root of the project, you won't find other .md files.

The .tpl.md files are normal markdown files with one addition: if you use ${[var]} within its text, [var] will be replaced by a var with the same name defined in buildvars.py when the corresponding md and.html files are generated.

If no variable with that name exists, the substitution doesn't take place.

This is useful for example to generate links and titles with the addon version included without having to rewrite documentation.

To translate documentation, grab the readme.tpl.md file at the root of the project and translate it. The translated file must be named readme.tpl.md and must be placed inside the addon/doc/[lang] directory.

The ${[xxx]} vars need to stay untouched. To generate the docs, issue scons and the markdown and HTML will be generated.
