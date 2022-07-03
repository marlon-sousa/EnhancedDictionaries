# EnhancedDictionaries ${addon_version}
Complemento do NVDA para lidar com processamento avançado de
dicionários

## download
Baixe o [Complemento Enhanced Dictionaries ${addon_version}](https://github.com/marlon-sousa/EnhancedDictionaries/releases/download/${addon_version}/EnhancedDictionaries-${addon_version}.nvda-addon)

## Recursos

### Dicionários específicos do perfil
A maneira que o NVDA implementa configurações condicionais, como a
formatação de documentos e outras é pelo uso de perfis.

Perfis são grupos de configurações que podem, em conjunto, ser aplicadas
condicionalmente no leitor de tela.

Por exemplo, você pode criar um perfil para programar, no qual o nível
de pontuação é tudo, anúncio de indentação é bips e a velocidade da fala
é mais lenta para que você leia código de uma maneira mais confortável.
Você pode, então, associar este perfil com o Visual Studio, Eclipse, notepad plus plus
e Visual Studio Code, a fim de que quando esses aplicativos forem executados as configurações
que você definiu anteriormente sejam aplicadas.

Quando você der alt tab para uma outra aplicação, ou quando você fechar
uma dessas aplicações e ir para a área de trabalho, por exemplo, a
configuração padrão tem efeito. É então possível facilmente alternar
entre o seu aplicativo para programar e o navegador e, sem pressionar
nenhuma outra tecla extra, ler sem pontuações no navegador e aplicar a
sua configuração específica quando estiver de volta ao ambiente de código.

Dicionários do NVDA são poderosos, oferecendo ótimas funções como
substituição por expressão regular. No entanto, atualmente não existe
nenhuma maneira de anexar dicionários aos perfis do NVDA.

Isto significa que se você configurar uma substituição no dicionário padrão, ela será applicada em todos os casos, mesmo em programas ou
situações específicas que você quisesse que elas não fossem.

Este complemento implementa o processamento e criação / edição de dicionários no contexto do perfil.

#### Como funciona?

Basta instalar o complemento. Quando ele está ativo:

* Dicionários são corretamente tratados tendo em vista o perfil atual.
* Se dicionários específicos (padrão ou voz) existirem para o perfil
atual, eles serão usados.
* Se eles não existirem, os dicionários do perfil padrão serão usados.

    Isto é consistente com a forma que o NVDA se comporta, no sentido de que quando se cria um novo perfil, as configurações que não são mudadas noperfil novo são pegas do perfil padrão.

    Similarmente, se não for configurado um dicionário para o perfil atual, o dicionário do perfil padrão será usado.

* Dicionários de voz funcionam exatamente dessa mesma forma: se existir
um dicionário de voz para o perfil atual, ele será usado. Do
contrário, o dicionário da voz do perfil padrão, se existir, será usado.
* O título da janela para configurar o dicionário mostra em qual perfil o dicionário está sendo editado.
* O perfil atualmente ativo determinará qual dicionário é editado quando os menus de dicionário padrão ou da voz forem ativados.

    Isto é consistente com a forma que o NVDA trabalha, uma vez que quando se muda uma configuração, ela é salva no perfil atual.

    Similarmente, o dicionário atualmente aberto irá pertencer a este perfil.

* Se um dado dicionário não existir para o perfil atual e a janela para configurar o dicionário for aberta, um novo dicionário para este perfil será criado. Como ele é um dicionário novo, iniciará vazio.

    No entanto, o dicionário não será salvo até que o usuário feche o diálogo clicando em "ok". Quando ele fizer isto, o novo dicionário entrará em efeito.

    Se o diálogo for cancelado, o dicionário padrão continuará em efeito e o dicionário atualmente sendo modificado não será salvo.

* Quando um novo dicionário específico para o perfil atual é criado, ele entra em efeito e, assim, as configurações feitas no dicionário padrão
deixarão de ser aplicadas.

    Este pode ser o comportamento esperado, mas talvez não.

    Talvez você queira usar as configurações do dicionário padrão mais as configurações feitas no dicionário do perfil atual.

* Para preencher esta lacuna, um botão "importar entradas do dicionário padrão" foi criado no diálogo de configurar o dicionário.

    Este botão aparece apenas quando um dicionário específico de perfil estiver sendo editado. Quando for ativado, ele funciona da seguinte maneira:

    - As entradas do dicionário padrão (ou dicionário específico de voz) do perfil padrão são lidas.
    - As entradas que não são encontradas no dicionário que está sendo editado são adicionadas a ele.
    - Se uma entrada do dicionário padrão (ou de voz) for encontrada no dicionário que está sendo editado, ela não substituirá a entrada atual.
    - A importação não salva as novas entradas no disco. Ela apenas adiciona entradas importadas na lista de entradas
    no diálogo de configurar o dicionário. O foco é colocado na lista e o usuário tem a oportunidade de revisar a nova lista de entradas, como se tivesse digitado
    manualmente todas elas.

* Sempre que o usuário cria um dicionário em um perfil específico, ele entra em efeito imediatamente para esse perfil.
* Sempre que um perfil muda, os dicionários específicos (padrão e voz) ficam ativos imediatamente.

    Se esses dicionários não existirem, os do perfil padrão são usados.

* Os dicionários interno e temporário do NVDA não são afetados, já que eles não dependem de perfis, o último por ser temporário e o primeiro por ser interno.

# ajudando a traduzir ou desenvolver o complemento

Se quiser ajudar a traduzir ou desenvolver o complemento, acesse o [repositório do projeto](https://github.com/marlon-sousa/EnhancedDictionaries) e busque pelo arquivo contributing.md no diretório de documentação equivalente ao seu idioma.

## Colaboradores

Agradecimentos a:

* Ângelo Miguel Abrantes - Tradução para Português
* Rémy Ruiz - Tradução para Espanhol
* Rémy Ruiz - Tradução para Francês
* Tarik Hadžirović - Tradução para Croata
*  Thiago Seus - Tradução para Português do Brasil
* Umut KORKMAZ - tradução para Turco
