# Contribuindo

## Gerando o complemento

Você vai precisar de:

* python 3.6 ou superior
* O pip deve estar configurado
* scons (pip install scons)
* markdown (pip install markdown)
* comando msgfmt. A maneira mais simples de obtê-lo é instalar o git e, na instalação, escolher a opção para tornar as ferramentas do bash disponíveis para o prompt de comandos

Uma vez que estes ítems estejam instalados, basta escrever scons na pasta raiz do projeto para gerar o complemento  

## Contribuindo traduções

### Traduzindo o complemento

Assumindo-se que você já tenha o ambiente configurado para construir o complemento (veja item acima), para gerar um arquivo pot de tradução basta escrever scons pot na pasta raiz do projeto.

A partir daí, é possível contribuir os arquivos po de tradução para seu idioma.

Os idiomas atualmente já traduzidos podem ser encontrados na pasta addon/docs/locale.

### Traduzindo documentação

As documentações de tradução devem ser geradas a partir de arquivos .tpl.md (não de arquivos .md).

Por isso, exceto pelo arquivo readme.md na raiz do projeto, você não encontrará outros arquivos .md versionados.

Os arquivos .tpl.md são arquivos markdown normais, exceto por um recurso a mais: se você usar ${[var]} em qualquer lugar do texto, [var] será substituído por uma variável com o mesmo nome ddefinida em buildVars.py.
Caso não haja uma variável com o mesmo nome, a substituição não acontece.

Isso é útil, por exemplo, para fazer com que a documentação reflita limks ou número de versão do complemento automaticamente, sem que precise ser reescrita.

Para traduzir a documentação, traduza o arquivo readme.tpl.md na raiz do projeto. O arquivo traduzido deve ser colocado na pasta addon/locale/[lang] e deve se chamar readme.tpl.md.

As variáveis ${[var]} não devem ser alteradas. Escreva scons na raiz do projeto para que a documentação HTML e markdown seja gerada.