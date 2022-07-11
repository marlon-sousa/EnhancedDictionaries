# EnhancedDictionaries ${addon_version}

Extra para lidar com um processamento de dicionários mais avançado

## Descarregar
Descarregar o [extra Enhanced Dictionaries ${addon_version}](https://github.com/marlon-sousa/EnhancedDictionaries/releases/download/${addon_version}/EnhancedDictionaries-${addon_version}.nvda-addon)

## Recursos

### Dicionários para perfis específicos 
A maneira como o NVDA aplica configurações condicionais, como formatação de documentos e outras, é através do uso de perfis.

Os Perfis são conjuntos de configurações que podem, momentaneamente, ser aplicados  ao leitor de ecrã, quando usamos dada aplicação ou grupo de aplicações .

Por exemplo, pode criar-se um perfil para aplicativos de escrita de código de programação, no qual o nível de pontuação é definido para "todos", o nível de indentação é definido para usar tons e a velocidade da voz é definida para um nível mais lento, para que se possa ler o código de maneira melhor e mais compreensiva.

É possível, então, associar este perfil ao "visual studio", ao "Eclipse", ao "notePad++" e ao "Visual Studio Code", para que, quando qualquer um destes aplicativos for activado, essas configurações sejam aplicadas automaticamente.

Com esta ferramenta, associada à faculdade que o NVDA nos oferece para criarmos perfis, quando nos movemos  para outros aplicativos ou quando fechamos um desses aplicativos e regressamos à  área de trabalho, por exemplo, volramos, sem que tenhamos que fazer mais nada, à configuração padrão.

Assim, torna-se possível, então, saltar facilmente do nosso aplicativo de codificação para um navegador e ler sem pontuações no navegador e aplicar as nossas configurações específicas, quando  voltarmos ao nosso ambiente de código de programação.

Os dicionários do NVDA são ferramentas poderosas, oferecendo ótimos recursos, como, por exemplo, a substituição de termos, usando expressões regulares.

No entanto,  até ao aparecimento deste extra, não havia como anexar dicionários a perfis no NVDA.

Até agora, Isto significava que, se  definisse uma substituição no dicionário padrão, ela seria aplicada em todos os casos, mesmo em aplicativos ou situações em que  desejasse que não fosse.

Este extra implementa o contexto do perfil ao processar e criar / editar dicionários.

#### Como funciona?

Instale o extra e quando ele estiver activo, observará o seguinte:

* Os dicionários agora são usados correctamente, tendo em consideração o perfil activo.
* Se existirem dicionários (padrão ou específicos da voz) para o perfil actual, eles serão usados.
* Se  não existirem dicionários específicos para o perfil que estamos a usar, os dicionários do perfil padrão serão usados.

    Isso é consistente com a maneira como o NVDA se comporta, no sentido de que quando eu crio um novo perfil, as configurações que eu não altero nesse novo perfil são retiradas do padrão. Da mesma forma, se eu não definir um dicionário para um perfil, o dicionário padrão será usado.

* Os dicionários de determinada voz comportam-se do modo anteriormente indicado.
* A caixa de diálogo do dicionário, quando aberta, mostra, no  título, a que perfil esse dicionário se refere.
* O perfil activo, quando carregado,  determinará qual o dicionário que será aberto para edição, quando os menus padrão ou de dicionário de voz forem activados.

    Isto é consistente com a maneira como o NVDA se comporta, porque se alguém aceder às configurações e alterar uma configuração, isso será guardado no perfil activo. Da mesma forma, o dicionário aberto pertencerá a esse perfil.

* Se um determinado dicionário não existir num perfil activo e a caixa de diálogo do dicionário for aberta, um novo dicionário para esse perfil será criado. Não mostrará quaisquer entradas, dado tratar-se de um dicionário novo.

    No entanto, não será guardado até que o utilizador feche a caixa de diálogo, clicando em "ok".

    Se procederem assim, o novo dicionário será eficaz. Se  cancelarem a caixa de diálogo, o dicionário de perfil padrão continuará a ser usado e nenhum dicionário específico de perfil será guardado.

* Quando um novo dicionário específico de perfil é criado, torna-se efectivo e, portanto, as configurações do dicionário padrão não estão mais activas para esse perfil.

    Esse pode ser o comportamento desejado, mas talvez não. Talvez o utilizador queira usar todas as configurações do dicionário padrão, para além das novas opções activas apenas nesse perfil.

* Para cobrir essa possibilidade, um novo botão, chamado "importar entradas do perfil padrão do dicionário", é criado na caixa de diálogo do dicionário.

    Este botão aparece apenas quando um dicionário específico do perfil está a ser editado. Na activação, comporta-se da seguinte maneira:
  
    - As entradas do dicionário padrão (ou do dicionário específico de voz), do perfil padrão, são lidas.
    - As entradas que não são encontradas no dicionário que está a ser editado são-lhe adicionadas.
    - Se uma entrada do dicionário padrão (ou de voz) for encontrada no dicionário que está a ser editado, não substituirá a entrada actual.
    - A importação não guarda as novas entradas no disco. Apenas adiciona entradas importadas na lista de entradas na caixa de diálogo do dicionário. O foco é colocado na lista e o utilizador tem a oportunidade de rever a nova lista de entradas, como se as tivesse escrito, manualmente, a todas elas.

* Sempre que o utilizador cria um dicionário para um perfil específico, esse dicionário é imediatamente associado a esse perfil.
* Sempre que um perfil muda, os seus dicionários específicos (padrão e de voz) ficam activos imediatamente. Se esses dicionários não existirem, os do perfil padrão serão usados.
* Os dicionários embutidos e temporários não são afectados, pois não dependem de perfis, o último por ser temporário e o primeiro por ser embutido.

# ajudando a traduzir ou desenvolver o extra

Se quiser ajudar a traduzir ou desenvolver o extra, acesse o [repositório do projeto](https://github.com/marlon-sousa/EnhancedDictionaries) e busque pelo arquivo contributing.md no diretório de documentação equivalente ao seu idioma.

## Colaboradores

Agradecimentos a:

* Ângelo Miguel Abrantes - Tradução para Português
* Rémy Ruiz - Tradução para Espanhol
* Rémy Ruiz - Tradução para Francês
* Tarik Hadžirović - Tradução para Croata
*  Thiago Seus - Tradução para Português do Brasil
* Umut KORKMAZ - tradução para Turco
* Ivan Shtefuriak - tradução para Ucraniana
