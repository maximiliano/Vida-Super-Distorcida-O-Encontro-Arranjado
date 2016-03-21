# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

define sd = Character('SD', color="#c8ffc8")
define anti = Character('ANTISSOCIAL', color="#990000")

# 1° ATO: INTRODUÇÃO
# Act 1: Introduction
label start:
    '1° ATO: INTRODUÇÃO'

    'SD esta dormindo em sua cama na manhã de sábado.\nO seu telefone já está alarmando a mais de uma hora e ele sequer o escutava. Todos tinham saído de casa e ele está só.'

    # O seu rosto e enquadrado em um zoom e começa a ser visto que ele está sonhando com um mudo de aventuras.

    sd 'Finalmente consegui todas as insígnias dos ginásios finalmente poderei me inscrever no torneio.'

    'De repente ouve-se um grande barulho: "Olha o carro do ovo, 10 ovos e um real...".'

    sd 'O que? Ovos...?'

    'SD acorda confuso e espantado escuta o resto da propaganda do carro do ovo que está passando.'

    sd 'Que coisa aquele sonho estava muito legal, esse carro tinha que passar logo agora.'

    'Ele escuta o alarme do celular tocando e diz:'

    sd 'Esse alarme ainda está tocando, mesmo colocando o telefone do lado de meu ouvido não consigo acordar com ele, que hora deve ser...'

    sd '...'

    # A imagem de SD segurando o telefone é exibida e a tela com a hora e focada exibindo: 9:37 AM.

    sd 'Ixi, já são mais de 9:30 tenho que levantar. Hoje vou continuar com aquele projeto do jogo digital do Homem Pomposo.'

    # Durante este comentário aparece a imagem imaginada de como seria a imagem do personagem do game e seu bigode mágico.
    # A cena e encerada com um FADE OUT.

    # É exibida uma sequência de imagens de SD executando os seus afazeres matinais e tomando café a manhã.

    sd 'Hoje não tem mais ninguém aqui em casa. Vou aproveitar o dia na paz...'

    # De repente o telefone toca e um alerta de mensagem e exibido. SD pega o aparelho para verificar, o conteúdo da mensagem e o seguinte:

    'De: Amigo X\nEi boy, uma prima minha viu o seu perfil naquela rede social e ficou interessada em lhe conhecer. Ela mora em uma cidade do interior e está aqui na cidade e me mediu para lhe perguntar se você tem compromisso para hoje.'

    # SD olha desconfiado e pensa:

    sd 'Que coisa. Deve ser alguma sacanagem por causa daquelas histórias que contei sobre nunca ter namorado ninguém.'

    # A imagem continua:
    '"E ai interessado? Ela e bonitinha dá uma olhada:"'

    # E exibida uma foto em anexo de uma garota morena, que possui cabelos rente aos ombros, olhos castanhos e uma face relativamente bonita e atraente.

    # SD pensa:
    sd 'Ate que e bonitinha, mas deve ser alguma brincadeira.'

    # Mais a baixo a mensagem continua.
    '"Você deve estar achando que é sacanagem minha mas para provar que estou falando sério veja esta selfie."'

    # Logo a baixo e exibida uma foto contendo com o Amigo X apontando para a mesma garota da foto anterior, que parecia envergonhada pela foto ter sido tirada sem que esperasse.

    # SD Pensa:

    sd 'Realmente parece que ele está falando a verdade. Esta foto não apresenta sinais de que foi alterada. Talvez seja uma experiência interessante.'

    # Mais a baixo a mensagem continua:

    '"O nome dela é Valkiria, se estiver interessado responda esta mensagem com uma sugestão do local e horário para o encontro. Ele tem que ser nesta tarde pois a noite ele já arrumará a bagagem para amanhã voltar para casa."'

    # SD se lembra que está tendo uma exposição de réplicas de artefatos egípcios em um shopping e pensa:

    sd 'Talvez convidá-la a ir ver a exposição de artefatos egípcios que está sendo exibida no shopping seja uma boa.'

    # SD começa a redigir a resposta a mensagem que fica da seguinte forma:

    'De: SD\nEu achei ela bem interessante, e como não tenho nenhum compromisso hoje, sugiro que o encontro seja no Shopping Sul, onde esta tendo uma exposição de artefatos egípcios, a qual podemos ir visitar. Estarei lá às 14:00 em frente a entrada da exposição.'

    # A mensagem e enviada e alguns minutos de pois chega a seguinte resposta:

    'De: Amigo X\nCombinado então, ela disse que visitar a exposição vai ser bastante interessante e que chegará la no horário combinado de 14:00.'

    # SD pensa:

    sd 'Espero que não seja nenhuma sacanagem. Melhor ir organizar as coisas e me arrumar para este encontro. Imagino como será a personalidade desta garota.'

    jump act_2

label act_2:

    '2° ATO: O ENCOSTO ANTISSOCIAL'
    'Apos receber a mensagem confirmando o encontro arranjado, uma visita inesperada aparece.'
    'Um ser de forma bizarra com aparência roliça de olhos grandes, sorriso largo e pele com uma coloração roxo acinzentado meio transparente, que SD chama de "ENCOSTO ANTISSOCIAL" começa a falar.'

    anti 'Ei você sabe claramente que isto deve ser apenas uma brincadeira de mau gosto deste seu "amigo".'

    sd 'A não você de novo, eu pensei que tinha se livrado de sua existência a meses atrás.'

    anti 'Rerere... Você sabe muito bem que eu sou parte de você e que sua insegurança com os "relacionamentos humanos" me fortalece. Ir a este suposto encontro é uma perda de tempo. É muito melhor a gente ficar em casa assistindo aqueles episódios de animes que saem hoje.'

    sd 'Eu estou cogitando isto, mas não posso passar mais 25 anos todo dia apenas sentado em uma cadeira de plástico rachada e desligado da realidade assistindo desenhos e escrevendo roteiros autobiográficos para tirinhas que fico enrolando para publicar e games de simuladores de relacionamento... Além do mais mesmo se esta garota não apareça eu estou querendo ver aquela exposição.'

    anti 'Sua lógica é bastante coerente, eu gostaria de vê-la também. Hoje eu irei lhe acompanhar.'

    sd '... Só o que faltava, um encosto interessado em obras de artes egípcias.'

    anti 'Quem disse que eu quero ver aqueles cacarecos. Estou interessado em ver a garota... Rerere...'

    sd 'Ferrou-se...'

    anti 'Espero que ela não queria que você não pague a entrada dela, pois se isto acontecer ficaremos sem dinheiro para compra o 10° volume daquele mangá neste mês.'

    sd 'Ixi... Tinha me esquecido, mas que seja. Talvez este seja um sinal de que devo mudar as minhas prioridades de temas fantasiosos para o complexo mundo real.'

    anti 'Você que sabe... Rerere...'

    sd 'Pensando bem, me pergunto se estou falando estas besteiras com você em voz alta ou apenas na minha imaginação. Pois se estiver falando alto os vizinhos devem estar achando que doido ou esquizofrênico.'

    anti 'Quem sabe talvez você esteja, talvez não. Mas com certeza você logo descobrirá... Rerere...'

    # Com esta última afirmativa a imagem do encosto desaparece da vista de SD, que pensa:

    sd 'Não devia ter tentado aquele método de criação de Tulpas (uma criatura materializada pelo pensamento humano que deve servir ao seu criador). Agora de vez em quando fica me aparecendo estas coisas estranhas.'

    # Após organizar algumas coisas SD, começa a se arrumar para sair.

    sd 'Está na hora de se arrumar. Vou tomar banho.'

    # _DESAFIO DO ATO 2: A ARANHA

    "Apos o banho o protagonista pega a toalha e nela esta uma enorme aranha armadeira, o que ele deve fazer?"

    # Dependendo da resposta a aranha picará o protagonista encerrando o jogo e exibindo uma imagem de derrota.

menu:
        'Tentar capturar a aranha.': # Falha, game over
            jump spider_fight_catch

        'Tenta matar a aranha com a toalha.': # Falha, mas o jogo continua
            jump spider_fight_kill

        'Joga a toalha para o outro lado do banheiro e fecha a porta.': # Sucesso
            jump spider_fight_escape

label spider_fight_catch:
    'Ao tentar capturar a aranha, ela pula no seu braço e te pica. Infelizmente você não ganha poderes, e agoniza envenenado até a sua morte.'
    'GAME OVER'
    return

label spider_fight_kill:
    $ spider_fight_choice = 'kill'
    'Você tenta bater com a toalha na parede para esmagar a aranha e ela escapa pulando, por sorte ela caí no sanitário.'
    'Você dá descarga e saí do banheiro.'
    jump after_spider_fight

label spider_fight_escape:
    $ spider_fight_choice = 'escape'
    'SUCESSO! A aranha agora está trancafiada no banheiro.'
    jump after_spider_fight


label after_spider_fight:
    'Continua...'

