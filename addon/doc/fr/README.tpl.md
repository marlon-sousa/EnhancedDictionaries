# EnhancedDictionaries ${addon_version}
Extension pour la gestion du traitement des dictionnaires plus avancés

## Télécharger
Télécharger l'extension [Enhanced Dictionaries ${addon_version}](https://github.com/marlon-sousa/EnhancedDictionaries/releases/download/${addon_version}/EnhancedDictionaries-${addon_version}.nvda-addon)

## Caractéristiques

### Dictionnaires pour des profils spécifiques
La manière dont NVDA applique les paramètres conditionnels, tels que la mise en Forme des Documents  et d'autres, c'est par l'utilisation de profils.

Les profils sont des ensembles de paramètres pouvant être  momentanément appliqués au lecteur d'écran, lorsque nous utilisons  une application particulière ou un groupe d'applications.

Par exemple, vous pouvez créer un profil,  pour des applications dédiés  à l'écriture de code de programmation, Dans lequel le niveau des ponctuations  est défini sur "tous", le niveau de la mise en retrait  est défini  sur "Des sons" et le débit de la parole est défini sur un niveau plus lent, afin que vous puissiez lire le code  d'de manière plus confortable. Vous pouvez ensuite associer ce profil avec "visual studio", "Eclipse", "notePad++" et "Visual Studio Code", lorsque l'une de ces applications deviennent actives, ces configurations s'appliqueront automatiquement.

Lorsque nous faisons Alt Tab pour aller à d'autres applications ou lorsque nous avons fermé l'une de ces applications et nous tombons  sur le bureau, par exemple, la configuration par défaut prends effet. C'est alors possible de passer facilement à partir  de notre application de codage et le navigateur, et sans appuyer sur aucune touche supplémentaire, de lire sans ponctuations dans le navigateur et que  notre configuration spécifique est appliquée lorsque nous sommes de retour dans notre environnement de code de programmation.

Les dictionnaires de NVDA sont des outils puissants, offrant d'excellentes fonctionnalités, telles que le remplacement de termes, en utilisant des expressions régulières. Cependant, jusqu'à l'apparition de cet extension, il n'y avait pas aucun moyen de rattacher de dictionnaires aux profils de NVDA.

Jusqu'à présent, cela signifiait que si un remplacement était défini dans le dictionnaire  Défaut, il serait appliqué dans tous les cas, même dans des applications ou des situations dans lesquelles vous pourriez souhaiter qu'ils ne le soient pas.

Cette extension implémente le traitement et la création / édition de dictionnaires dans le contexte du profil.

#### Comment ça marche?

Simplement installer l'extension et lorsqu'elle est active, vous remarquerez les points suivants:

* Les dictionnaires sont maintenant utilisés correctement, en tenant compte du profil actif.
* S'il y a des dictionnaires (Défaut ou spécifique à la voix) pour le profil actuel, ils seront utilisés.
* S'il n'y a pas de dictionnaires spécifiques pour le profil que nous utilisons, les dictionnaires de profil par défaut seront utilisés. Ceci est cohérent avec la façon dont NVDA se comporte, dans le sens où lorsqu'un nouveau profil est créé, les configurations ne sont pas modifiées dans ce nouveau profil en prenant le profil par défaut.

    De même, si un dictionnaire n'est pas configuré pour le profil actuel, le dictionnaire de profil par défaut sera utilisé.

* Les dictionnaires spécifique à la voix se comportent exactement de la même manière: S'il y a un dictionnaire de voix pour le profil actuel, il sera utilisé. Sinon, le dictionnaire de voix du profil par défaut, s'il existe, sera utilisé.
* La boîte de  dialogue de dictionnaire , lorsqu'elle est ouverte, montre toujours dans le titre, à quel profil de ce dictionnaire se réfère.
* Le profil actif, lorsqu'il est chargé, déterminera quel dictionnaire sera ouvert pour l'édition, lorsque les menus de dictionnaire  Défaut  ou de Voix sont activés.

    Ceci est cohérent avec la manière dont NVDA se comporte, car si une personne accède à la configuration  et elle est modifiée, cela sera  sauvegardé sur le profil actif.

    De même, le dictionnaire ouvert appartiendra à ce profil.

* Si un dictionnaire spécifique n'existe pas sur un profil actif et que la boîte de dialogue de dictionnaire est ouverte, un nouveau dictionnaire pour ce profil sera créé.

    Ceci ne montrera aucune entrée, étant donné être un nouveau dictionnaire. Cependant, il ne sera pas sauvegardé avant que l'utilisateur ferme cette boîte de dialogue en cliquant sur "OK".

    Si nous procédons ainsi , le nouveau dictionnaire sera effectif. Si nous annulons la boîte de dialogue, le dictionnaire de profil par défaut sera toujours utilisé et aucun dictionnaire spécifique au profil ne sera sauvegardé.

* Lorsqu'un nouveau dictionnaire spécifique de profil est créé, il devient effectif et, par conséquent, les modèles  par défaut ne sont plus actifs pour ce profil.

    Cela pourrait être le comportement souhaité, mais peut-être pas. L'utilisateur souhaite peut-être utiliser tous les modèles à partir du dictionnaire par défaut et de nouveaux modèles uniquement actifs sur ce profil.

* Pour couvrir cette possibilité, un nouveau  bouton, appelé "Importer des entrées à partir du profil du dictionnaire par défaut", est créée dans la boîte de dialogue de dictionnaire.

    Ce bouton apparaît uniquement lorsqu'un dictionnaire spécifique au profil est édité. Pendant l'activation, il se comporte comme suit:
  
    - Les entrées du dictionnaire Défaut (ou du dictionnaire spécifique à la voix) à partir du profil par défaut sont lues.
    - Les entrées introuvables dans le dictionnaire étant éditées sont ajoutées à celui-ci.
    - Si une entrée du dictionnaire  Défaut (ou voix) se trouve sur le dictionnaire étant édité, elle ne remplace pas l'entrée actuelle.
    - L'importation ne sauvegarde pas les nouvelles entrées sur le disque. Il ajoute simplement des entrées importées dans la liste des entrées dans la boîte de dialogue de dictionnaire. Le focus est mis sur la liste et l'utilisateur a la possibilité d'examiner la nouvelle liste  d'entrées, Comme s'il les avait tous écrite manuellement.

* Chaque fois que l'utilisateur crée un dictionnaire pour un profil spécifique, ce dictionnaire est immédiatement associé à ce profil.
* Chaque fois qu'un profil change, les dictionnaires spécifiques (Défaut et Voix) deviennent actifs immédiatement. Si ces dictionnaires n'existent pas, ceux du profil par défaut seront utilisés.
* Les dictionnaires intégrés et temporaires ne sont pas affectés car ils ne dépendent pas des profils, le dernier pour être temporaire et le premier pour être intégré.

# aidant à traduire ou à développer l'extension

Si vous voulez aider à traduire ou à développer l'extension, s'il vous plaît accéder au  [dépôt du projet](https://github.com/marlon-sousa/EnhancedDictionaries) et recherchez le fichier contributing.md dans le répertoire de documentation équivalent à votre langue.

## Contributeurs

Remerciement spécial à

* Ângelo Miguel Abrantes - Traduction Portugais Portugal
* Rémy Ruiz - Traduction Français
* Rémy Ruiz - Traduction Espagnol
*  Thiago Seus - Traduction Portugais Brésil
* Umut KORKMAZ - Traduction turc
