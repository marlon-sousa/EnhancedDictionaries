# Contribuant

## Générer l'extension

Vous aurez besoin de:

* python 3.6 ou supérieur
* pip doit être configuré
* scons (pip install scons)
* markdown (pip install markdown)
* commande msgfmt. Le moyen le plus simple de l'obtenir est d'installer git et, de choisir l'option pour créer les outils Bash disponibles pour l'invite de commande

Une fois que ces éléments sont installés, écrivez simplement  scons dans la racine du dossier du projet pour générer l'extension

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
