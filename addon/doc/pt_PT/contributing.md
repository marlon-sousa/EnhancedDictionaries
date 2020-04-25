# Contribuir

## Criar  o extra

Para  isso, vai precisar de:

* python 3.6 ou superior
* O pip deve estar configurado
* scons (pip install scons)
* markdown (pip install markdown)
* comando msgfmt. A maneira mais simples de obtê-lo é instalar o git e, na instalação, escolher a opção para tornar as ferramentas do bash disponíveis para o prompt de comandos

Uma vez que estes ítems estejam instalados, basta escrever scons na pasta raíz do projecto para criar o extra  

## Contribuir para as traduções

### Traduzir o extra

Assumindo que já tenha o ambiente configurado para construir o extra (veja item acima), para criar um ficheiro ".pot", onde ficarão todas as mensagens para a  tradução, basta escrever scons pot, na pasta raíz do projecto.

A partir deste ficheiro base, é possível construir os ficheiros ".po" de tradução para o seu idioma.

Os idiomas  já traduzidos podem ser encontrados na pasta addon/docs/locale.

### Traduzir a documentação

As documentações de tradução devem ser geradas a partir de ficheiros ".tpl.md" (não de ficheiros ".md").

Por isso, excepto no ficheiro "readme.md", na raíz do projecto, não encontrará outros ficheiros ".md" versionados.

Os ficheiros ".tpl.md" são ficheiros markdown normais, excepto por um recurso a mais: se  usar ${[var]} em qualquer lugar do texto, [var] será substituído por uma variável com o mesmo nome ddefinida em buildVars.py.
Caso não haja uma variável com o mesmo nome, a substituição não acontece.

Isto é útil, por exemplo, para fazer com que a documentação reflicta limks ou número de versão do extra automaticamente, sem que precise ser reescrita.

Para traduzir a documentação, traduza o ficheiro "readme.tpl.md", na raíz do projecto. O ficheiro traduzido deve ser colocado na pasta addon/locale/[lang] e deve chamar-se "readme.tpl.md".

As variáveis ${[var]} não devem ser alteradas. Escreva scons na raíz do projecto para que a documentação HTML e markdown seja criada.