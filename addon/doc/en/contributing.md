# Contributing

## building the addon

You will need:

* python 3.11 or above.
* pip must be configured
* scons (pip install scons)
* markdown (pip install markdown)
* pre-commit (pip install pre-commit)
* msgfmt utility. The easiest way of getting it is by installing git bash and choosing to include bash tools at command prompt

At the very first time you clone the repository, perform a 
```
pre-commit install
```

to make sure pre-commit hooks are installed.

If there are quality failures, commits won't be allowed.

You can perform a pre test before commiting at any time by issuing

```
pre-commit run --all-files
```

Warning: if you do not install githooks (e.e issuing pre-commit install), your commits won't be cjhecked.  
However, when submiting a pull request, there are checks that will block your commits if they fail passing pre-commit hooks. It is always best to fix quality issues before commiting.

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
