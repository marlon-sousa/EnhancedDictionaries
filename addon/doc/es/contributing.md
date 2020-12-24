# Contribuir

## Crear el complemento

Para esto, necesitarás:

* python 3.6 o superior
* El pip debe estar configurado
* scons (pip install scons)
* markdown (pip install markdown)
* comando msgfmt. La forma más sencilla de obtener es instalar el git y, en la instalación, elija la opción para que las herramientas Bash estén disponibles para el símbolo del sistema

Una vez que estos elementos están instalados, basta escribir scons en la carpeta raíz del proyecto para crear el complemento

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
