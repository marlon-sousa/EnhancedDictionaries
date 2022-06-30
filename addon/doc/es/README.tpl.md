# EnhancedDictionaries ${addon_version}
Complemento de NVDA para la gestión del procesamiento de diccionarios más avanzado

## Descargar
Descargar el complemento [Enhanced Dictionaries ${addon_version}](https://github.com/marlon-sousa/EnhancedDictionaries/releases/download/${addon_version}/EnhancedDictionaries-${addon_version}.nvda-addon)

## Características

### Diccionarios específicos de perfil
La forma en que NVDA implementa configuraciones condicionales, tal como  el formateado de documentos y otros es utilizando perfiles.

Los perfiles son grupos de configuraciones que pueden ser aplicadas temporalmente al lector de pantalla, cuando usamos una aplicación en particular o un grupo de aplicaciones.

Por ejemplo, puedes  crear un perfil para aplicaciones dedicadas a la escritura de códigos de programación, en el que el nivel de puntuación se establece en "toda", el anuncio de sangría se establece en "Tonos" y la velocidad de la voz  se establece en velocidad más lenta para que se lea el código de una manera más cómoda. Luego puedes asociar este perfil con "Visual Studio", "Eclipse", "notepad plus plus" y "Visual Studio Code", De modo que cuando cualquiera de estas aplicaciones se active, estas configuraciones se aplicarán automáticamente.

Cuando haces Alt Tab para pasar a otras aplicaciones, o cuando cierras una de estas aplicaciones y caes en el escritorio , por ejemplo, la configuración  predeterminada tiene efecto. Luego, es fácil de cambiar entre  tu aplicativo para programar y el navegador y, sin presionar ninguna otra tecla adicional, de leer sin puntuación en el navegador y se aplica a tu configuración específica cuando estás de vuelta en    tu entorno de códigos de programación.

Los diccionarios de NVDA son poderosos, ofreciendo excelentes funciones, como reemplazar la expresión regular. Sin embargo, hasta la aparición de  este complemento no había  forma de colocar diccionarios a los perfiles de NVDA.

Esto significa que si configuras una sustitución en el diccionario predeterminado, se aplicará en todos los casos, incluso en programas o situaciones específicas que quisieras que no lo sean.

Este complemento implementa el procesamiento y creación / edición de los diccionarios en el contexto del perfil.

#### ¿Como funciona?

Basta instalar el complemento. Cuando está habilitado, notarás los siguientes puntos:

* Los diccionarios se tratan correctamente Tomando en consideración el perfil actual.
* Si existen diccionarios específicos (predeterminados o voz) para el perfil actual, se utilizarán.
* Si no existen, se utilizarán los diccionarios de perfil predeterminados. Esto es consistente con la forma en que se comporta NVDA, en el sentido de que cuando se crea un nuevo perfil, Las configuraciones no se  cambia en este nuevo perfil tomandose del perfil predeterminado.

    De manera similar, si un diccionario no está configurado para el perfil actual, se utilizará el diccionario de perfil predeterminado.

* Los diccionarios de voz trabajan exactamente de la misma manera: si hay un diccionario de voz para el perfil actual, se utilizará. De lo contrario, el diccionario de  voz del perfil predeterminado, si existe, se utilizará.
* El título de la ventana para configurar el diccionario muestra en qué perfil se está editando el diccionario.
* El perfil actualmente activo determinará en qué diccionario  se está editando cuando los menús de diccionario predeterminados o de voz están habilitados.

    Esto es consistente con la forma en que funciona NVDA, ya que cuando se cambia una configuración, se guarda en el perfil actual.

    Del mismo modo, el diccionario actualmente abierto pertenecerá a este perfil.

* Si un diccionario dado no existe para el perfil actual y la ventana para configurar el diccionario está abierta, se creará un nuevo diccionario para este perfil.

    Como es un nuevo diccionario, comenzará vacío. Sin embargo, el diccionario no se guardará hasta que el usuario cierra el diálogo haciendo clic en "Aceptar".

    Cuando lo haga, el nuevo diccionario entrará en efecto . Si se cancela el diálogo, el diccionario predeterminado continuará efectivo y el diccionario que se está modificando actualmente no se guardará.

* Cuando se crea un nuevo diccionario específico de perfil, se vuelve efectivo y, por lo tanto, los patrones en el diccionario predeterminado ya no están activos para ese perfil.

    Este puede ser el comportamiento esperado, pero tal vez no. Es posible que el usuario  desee utilizar todos los patrones del diccionario  predeterminado más los nuevos patrones sólo activos en este perfil.

* Para colmar esta brecha, se creó un botón llamado "Importar entradas a partir del perfil de diccionario predeterminado", en el cuadro de diálogo del diccionario.

    Este botón aparece solo cuando se está editando un diccionario de perfil específico. Cuando se activa, funciona de la siguiente manera:

    - Se leen las entradas del diccionario predeterminado (o el diccionario específico de voz) del perfil predeterminado.
    - Se añaden las entradas que no se encuentran en el diccionario que se está editando.
    - Si se encuentra una entrada de diccionario predeterminado (o voz) en el diccionario que se está editando, no reemplazará la entrada actual.
    - La importación no guarda las nuevas entradas en el disco. Ella solo añade entradas importadas en la lista de entradas en el cuadro de diálogo del diccionario. El foco se coloca en la lista y el usuario tiene la oportunidad de revisar la nueva lista de entradas, como si lo había digitado manualmente todas ellas.

* Cada vez que el usuario crea un diccionario en un perfil específico, se asocia inmediatamente con este perfil.
* Siempre que cambie un perfil, los diccionarios específicos (predeterminado y voz) están activos de inmediato. Si estos diccionarios no existen, los del perfil predeterminado se utilizan.
* Los diccionarios internos y temporales de NVDA no se ven afectados, ya que no dependen de los perfiles, lo último por ser temporal y el primero por ser interno.

# ayudando a traducir o desarrollar el complemento

Si deseas ayudar a traducir o desarrollar el complemento, por favor  acceda al [repositório del proyecto](https://github.com/marlon-sousa/EnhancedDictionaries) y buscar el archivo contributing.md en el directorio de documentación equivalente a tu idioma.

## Contribuidores

Agradecimientos especiales a

* Ângelo Miguel Abrantes - Traducción Portugués
* Rémy Ruiz - Traducción Francés
* Rémy Ruiz - Traducción Español
*  Thiago Seus - Traducción Portugués del Brasil
* Umut KORKMAZ - Traducción turco
