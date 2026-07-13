# Contribuir

## Crear el complemento

Para esto, necesitarás:

* python 3.13.
* El pip debe estar configurado
* scons (pip install scons)
* markdown (pip install markdown)
* gettext, que proporciona las utilidades `msgfmt` y `xgettext`. `msgfmt` compila los archivos de traducción en cada compilación, y `xgettext` es utilizado por `scons pot` para generar la plantilla de traducción. En Windows, instala una versión moderna desde [gettext-iconv-windows](https://github.com/mlocati/gettext-iconv-windows/releases) (o usa `scoop install gettext` / `choco install gettext`), y asegúrate de que su directorio `bin` esté antes que cualquier otro gettext en tu PATH. No uses el paquete gettext de GnuWin32: está congelado en la versión 0.14.4 (2005) y es demasiado antiguo para esta compilación (`scons pot` falla por la opción no soportada `--package-name`).

Una vez que estos elementos están instalados, basta escribir scons en la carpeta raíz del proyecto para crear el complemento

### Pre-commit

Se recomienda encarecidamente que instales pre-commit.

* pip install pre-commit
* pre-commit install

Esto instala pre-commit y configura sus hooks, de modo que cada vez que realices un commit se aplicarán varias comprobaciones. Si alguna de ellas falla, el commit no se permitirá.

Puedes ejecutar las comprobaciones de pre-commit en cualquier momento sin realizar un commit ejecutando "pre-commit run --all-files".

### Flake8

Uno de los hooks de pre-commit es Flake8, un linter de Python que, entre otras cosas, ayuda a garantizar que el proyecto tenga un formato coherente y que se sigan buenas prácticas.

El hook Flake8 de pre-commit usa la misma configuración de `flake8.ini`.

## Contribuir para las traducciones

### Traducir el complemento

Suponiendo que ya tienes el entorno configurado para construir el complemento (consulta la sección anterior), para crear un archivo ".pot", donde todos los mensajes serán para la traducción, basta escribir scons pot, en la carpeta raíz del proyecto.

A partir de este archivo base, puedes construir los archivos ".po" de traducción para tu idioma.
Los idiomas ya traducidos se pueden encontrar en la carpeta /addon/locale.

### Traducir la documentación

La documentación de traducción debe generarse a partir de los archivos ".tpl.md" (no de los archivos ".md"). Por lo tanto, excepto en el archivo  "readme.md", en la raíz del proyecto, no encontrarás otros archivos ".md" versionados.

Los archivos ".tpl.md" son archivos markdown normales, excepto por una característica adicional: si  usas ${[var]} en cualquier lugar del texto, [var] será reemplazado  por una variable con el mismo nombre definido en el buildVars.py.

Si no hay una variable con el mismo nombre, el reemplazo no sucede.

Esto es útil, por ejemplo, para hacer que la documentación refleje los enlaces y títulos con el número de versión  del complemento automáticamente, sin necesidad de  ser reescrita.

Para traducir la documentación, tradusca el archivo "readme.tpl.md", en la raíz del proyecto. El archivo traducido debe colocarse en la carpeta addon/doc/[lang] y debe llamarse "readme.tpl.md".

Las variables ${[var]} no deben cambiarse. Escriba scons en la raíz del proyecto para que la documentación HTML y markdown sea creada.
