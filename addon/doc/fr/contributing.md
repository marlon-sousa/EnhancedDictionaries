# Contribuant

## Générer l'extension

Vous aurez besoin de:

* python 3.13.
* pip doit être configuré
* scons (pip install scons)
* markdown (pip install markdown)
* gettext, qui fournit les utilitaires `msgfmt` et `xgettext`. `msgfmt` compile les fichiers de traduction à chaque génération, et `xgettext` est utilisé par `scons pot` pour générer le modèle de traduction. Sous Windows, installez une version moderne depuis [gettext-iconv-windows](https://github.com/mlocati/gettext-iconv-windows/releases) (ou utilisez `scoop install gettext` / `choco install gettext`), et assurez-vous que son répertoire `bin` se trouve avant tout autre gettext dans votre PATH. N'utilisez pas le paquet gettext de GnuWin32 : il est figé à la version 0.14.4 (2005) et est trop ancien pour cette génération (`scons pot` échoue à cause de l'option non prise en charge `--package-name`).

Une fois que ces éléments sont installés, écrivez simplement  scons dans la racine du dossier du projet pour générer l'extension

### Pre-commit

Il est fortement recommandé d'installer pre-commit.

* pip install pre-commit
* pre-commit install

Ceci installe pre-commit et configure ses hooks, de sorte que chaque fois que vous effectuez un commit, plusieurs vérifications s'appliquent. Si l'une d'elles échoue, le commit ne sera pas autorisé.

Vous pouvez lancer les vérifications de pre-commit à tout moment sans effectuer de commit en exécutant « pre-commit run --all-files ».

### Flake8

L'un des hooks de pre-commit est Flake8, un linter Python qui, entre autres, aide à garantir que le projet a un formatage cohérent et que les bonnes pratiques sont respectées.

Le hook Flake8 de pre-commit utilise la même configuration depuis `flake8.ini`.

## Contribuant aux traductions

### Traduisant l'extension

En supposant que vous ayez déjà l'environnement configuré pour construire l'extension (voir la section ci-dessus), pour générer un fichier ".pot" où tous les messages seront pour la traduction, écrivez simplement scons pot dans la racine du dossier du projet.

À partir de ce fichier de base, vous pouvez générer les fichiers ".po" de traduction  pour votre langue.
Les langues actuellement traduites peuvent être trouvées dans le dossier /addon/locale.

### Traduisant la documentation

La documentation de traduction doit être générée à partir des fichiers ".tpl.md" ((pas des fichiers ".md"). Par conséquent, à l'exception du fichier "readme.md", dans la racine du projet, vous ne trouverez pas d'autres fichiers ".md" versionnés.

Les fichiers ".tpl.md" sont des fichiers markdown normaux, Sauf pour  une fonctionnalité en plus: si vous utilisez ${[var]} n'importe où dans le texte, [var] sera remplacé par une variable avec le même nom défini dans  le buildVars.py.

S'il n'y a pas de variable avec le même nom, le remplacement ne se produit pas.

Ceci est utile, par exemple, pour faire que la documentation reflète les liens et titres avec le numéro de version  de l'extension automatiquement, sans besoin d'être réécrite.

Pour traduire la documentation, traduisez le fichier "readme.tpl.md", dans la racine du projet. Le fichier traduit doit être placé dans le dossier addon/doc/[lang] et doit être appelé "readme.tpl.md".

Les variables ${[var]} ne doivent pas être modifiées. Écrivez  scons dans la racine du projet afin que la documentation  HTML et markdown soit générée.
