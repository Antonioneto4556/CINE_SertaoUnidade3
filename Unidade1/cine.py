# ===== APRESENTAÇÃO DO PROGRAMA ===== #

from time import sleep

usuarios = {'Antonio': {'senha': 'neto123', 'perfil': 'admin'},
            'Neto': {'senha': '123', 'perfil': 'cliente'}
            }
salas = set()
filmes = {'Jalin Habei': {'sala': 1, 'horario': '18:00', 'capacidade': 75, 'valor': 60.00, 'ingressos_vendidos': 0},
          'Tomas Turbano2': {'sala': 2, 'horario': '19:30', 'capacidade': 80, 'valor': 69.00, 'ingressos_vendidos': 0},
          'Sherek 6': {'sala': 3, 'horario': '20:15', 'capacidade': 90, 'valor': 50.00, 'ingressos_vendidos': 0},
          'Naruto Usacrak': {'sala': 4, 'horario': '20:15', 'capacidade': 60, 'valor': 40.00, 'ingressos_vendidos': 0},
          'O Banheiro': {'sala': 5, 'horario': '20:15', 'capacidade': 75, 'valor': 50.00, 'ingressos_vendidos': 0},
          }
for filme in filmes.values():
    salas.add(filme['sala'])
while True:
    print('\n\033[95:40m}======[ \033[m\033[1:3:97:40mCINE-SERTÃO\033[m\033[95:40m ]======{\033[0m')
    print('\033[7:91:40m[ 1 ]\033[m\033[7:94:40m | GERENCIAR OS FILMES |\033[m')
    print('\033[7:91:40m[ 2 ]\033[m\033[94:40m | COMPRAR  INGRESSOS  |\033[m')
    print('\033[7:91:40m[ 3 ]\033[m\033[7:94:40m | FILMES  EM  CARTAZ  |\033[m')
    print('\033[7:91:40m[ 4 ]\033[m\033[94:40m | CADASTRAR  USUARIO  |\033[m')
    print('\033[7:90:40m[ 0 ]\033[m\033[7:91:40m | SAIR   DO   MENU    |\033[m')

    opcaoM = int(input(f'\033[1:3:7:40m Escolha uma opção:          \033[m'))
    print()
    if(opcaoM == 1):
        sleep(1)
        while True:
            print('\033[1:3:7:91:40m ===== [ADMINISTRAÇÂO] ===== \033[m')
            usuario = input('Digite o nome de usuário: ')
            senha = input('Digite a senha: ')
            if(usuario in usuarios and usuarios[usuario]['senha'] == senha):
                print('Login bem-sucedido!')
                break
            else:
                print('\033[91mUsuário ou senha incorretos. Tente novamente.\033[m')

        if(usuarios[usuario]['perfil'] == 'admin'):
            while True:
                print('\n\033[94m=== Módulo de Gerenciamento de Filmes ===\033[0m')
                print('\033[0:91:40m[1]\033[m\033[1:3:7:97:40m [Cadastrar Filme]     \033[m')
                print('\033[0:91:40m[2]\033[m\033[1:3:7:97:40m [Buscar Filme]        \033[m')
                print('\033[0:91:40m[3]\033[m\033[1:3:7:97:40m [Atualizar Filme]     \033[m')
                print('\033[0:91:40m[4]\033[m\033[1:3:7:97:40m [Remover Filme]       \033[m')
                print('\033[0:91:40m[5]\033[m\033[1:3:7:97:40m [Vendas de ingressos] \033[m')
                print('\033[0:91:40m[0]\033[m\033[1:3:7:97:40m [Menu principal]      \033[m')

                opcao = int(input('\033[1:3:6:7:94:40m #Escolha uma opção:      \033[m'))
                if(opcao == 1):
                    sleep(1)
                    print('\n\033[1:3:7:93:40mCADASTRO DE FILMES\033[m')
                    titulo = input('Título do Filme: ')
                    sala = int(input('Sala: '))
                    while sala in salas:
                        print('\033[91mSala já cadastrada\033[m. \033[94mEscolha outra sala\033[m.')
                        sala = int(input('Sala: '))
                    salas.add(sala)
                    horario = input('Horário: ')
                    capacidade = int(input('Capacidade: '))
                    valor = float(input('Valor do Ingresso: '))
                    filmes[titulo] = {'sala': sala,'horario': horario,'capacidade': capacidade,
                                      'valor': valor,'ingressos_vendidos': 0}
                    print('\033[92mFilme cadastrado com sucesso!\033[m')
                elif(opcao == 2):
                    sleep(1)
                    print('\n\033[1:3:7:93:40mBUSCAR FILME\033[m')
                    titulo = input('Digite o título do filme: ')
                    if(titulo in filmes):
                        print('\033[92mFilme encontrado:\033[m')
                        print(filmes[titulo])
                    else:
                        filmes_similares = []
                        for filme_titulo in filmes.keys():
                            if(titulo.lower() in filme_titulo.lower()):
                                filmes_similares.append(filme_titulo)
                        if(filmes_similares):
                            print('\033[91mFilme não encontrado\033[m. \033[94mFilmes semelhantes:\033[m')
                            for filme in filmes_similares:
                                print(filme)
                                sleep(1)
                        else:
                            print('\033[91mFilme não encontrado.\033[m')
                elif(opcao == 3):
                    sleep(1)
                    print('\n\033[1:3:7:93:40mATUALIZAÇÃO DE FILMES\033[m')
                    titulo = input('Digite o título do filme que deseja atualizar: ')
                    if(titulo in filmes):
                        print('\033[92mFilme encontrado\033[m. \033[94mAtualize as informações\033[m: ')
                        filmes[titulo]["sala"] = input('Nova Sala: ')
                        filmes[titulo]["horario"] = input('Novo Horário: ')
                        filmes[titulo]["capacidade"] = int(input('Nova Capacidade: '))
                        filmes[titulo]["valor"] = float(input('Novo Valor do Ingresso: '))
                        print('Filme atualizado com sucesso!')
                    else:
                        Moves_semelhantes = []
                        for filme_titulo in filmes.keys():
                            if(titulo.lower() in filme_titulo.lower()):
                                Moves_semelhantes.append(filme_titulo)
                        if(Moves_semelhantes):
                            print('\033[91mFilme não encontrado\033[m. \033[96mFilmes semelhantes:\033[m')
                            for filme in Moves_semelhantes:
                                print(filme)
                            sleep(1)
                        else:
                            print('\033[91mFilme não encontrado\033[m.')
                            sleep(1)
                elif(opcao == 4):
                    print('\n\033[1:3:7:93:40mREMOVER FILMES\033[m')
                    titulo = input('Digite o título do filme que deseja remover: ')
                    if(titulo in filmes):
                        del filmes[titulo]
                        print('\033[92mFilme removido com sucesso\033[m!')
                    else:
                        Moves_semelhantes = []
                        for filme_titulo in filmes.keys():
                            if(titulo.lower() in filme_titulo.lower()):
                                Moves_semelhantes.append(filme_titulo)
                        if(Moves_semelhantes):
                            print('\033[91mFilme não encontrado\033[m. \033[96mFilmes semelhantes\033[m:')
                            for filme in Moves_semelhantes:
                                print(filme)
                            sleep(1)
                        else:
                            print('\033[91Filme não encontrado\033[m.')
                            sleep(1)
                elif (opcao == 5):
                    print('\n\033[1:3:7:93:40mVENDAS DE INGRESSO\033[m')
                    total_receita = 0
                    for titulo, filme in filmes.items():
                        ingressos_vendidos = filme['ingressos_vendidos']
                        valor_total = ingressos_vendidos * filme['valor']
                        total_receita += valor_total
                        print(
                            f'Filme: \033[93m{titulo}\033[m, Ingressos Vendidos: \033[91m{ingressos_vendidos}\033[m, Valor Total Arrecadado:\033[92m R$ {valor_total:.2f}\033[m')
                        sleep(1)
                    print(f'Total de receita: \033[92mR$ {total_receita:.2f}\033[m')
                elif(opcao == 0):
                    sleep(1)
                    break
                else:
                    print('\033[91Opção inválida\033[m!')
        else:
            print('\033[mAcesso negado! Esta função é exclusiva para administradores\033[m.')

    elif(opcaoM == 2):
        sleep(1)
        print('\033[1:3:7:93:40m === COMPRA DE INGRESSOS === \033[m')
        while True:
            usuario = input('Digite o nome de usuário: ')
            senha = input('Digite a senha: ')
            if(usuario in usuarios and usuarios[usuario]['senha'] == senha):
                print('\033[92mLogin bem-sucedido\033[m!')
                break
            else:
                print('\033[91mUsuário ou senha incorretos\033[m.\033[94m Tente novamente\033[m.')

        if(usuarios[usuario]['perfil'] == 'cliente'):
            print('\n\033[1:3:7:95:40m#=-COMPRA DE INGRESSOS-=#\033[m')
            print('Filmes Disponíveis:')
            for titulo, filme in filmes.items():
                print(f'\033[94m{titulo}\033[m - \033[92mR$\033[m \033[91m{filme['valor']:.2f}\033[m')
            titulo = input('\033[1:7:90:40mDigite o título completo: \033[m')
            if(titulo in filmes):
                filme = filmes[titulo]
                if(filme['capacidade'] > 0):
                    filme['capacidade'] -= 1
                    filme['ingressos_vendidos'] += 1
                    print(f'\033[92mIngresso comprado com sucesso para {titulo}. Aproveite o filme!\033[m')
                else:
                    print('\033[93mDesculpe, a capacidade máxima para este filme foi atingida.\033[m')
            else:
                Moves_semelhantes = []
                for filme_titulo in filmes.keys():
                    if(titulo.lower() in filme_titulo.lower()):
                        Moves_semelhantes.append(filme_titulo)
                if(Moves_semelhantes):
                    print('\033[91mFilme não encontrado\033[m.\033[94m Filmes semelhantes\033[m:')
                    for filme in Moves_semelhantes:
                        print(filme)
                else:
                    print('\033[91mFilme não encontrado.\033[m')
                    sleep(1)
        else:
            print('\033[1:3:7:95:40mMas apenas clientes podem comprar ingressos!\033[m')
            sleep(1)

    elif(opcaoM == 3):
        sleep(1)
        while True:
            print('\033[97m-=\033[m'*34)
            print('\033[1:3:7:93:40m === FILMES  DISPONÍVEIS === \033[m')
            print('\033[97m-=\033[m' * 34)
            for titulo, filme in filmes.items():
                print(f'\033[94m{titulo}\033[m - \033[94m{filme['sala']}\033[m - \033[91m{filme['horario']}\033[m - \033[92mR$ {filme['valor']:.2f}\033[m - \033[96m{filme['capacidade']} lugares disponíveis\033[m')
            voltandoM = str(input('Digite \033[92m[V]\033[m para volta ao \033[92mMENU\033[m:')).upper()
            if(voltandoM == 'V'):
                sleep(1)
                break
            else:
                sleep(1)
    elif(opcaoM == 4):
        (sleep(1))
        while True:
            print('\033[1:3:7:93:40m ======== CADASTROS ======== \033[m')
            novo_usuario = input('Nome de Usuário: ')
            if(novo_usuario not in usuarios):
                senha = input('Senha: ')
                perfil = input('Perfil [admin] ou [cliente]: ')
                usuarios[novo_usuario] = {'senha': senha, 'perfil': perfil}
                print('\033[92m Usuário cadastrado com sucesso!\033[m')
                novo_registro = int(input('''\033[1:3:7:93:40m[1]\033[m\033[1:3:7:97:40m Para cadastra novamente;   \033[m
\033[1:3:7:93:40m[2]\033[m\033[1:3:7:97:40m Caso queira voltar ao menu;\033[m
\033[1:3:7:97:40m                        \033[m\033[1:3:7:90:42m OPÇÃO:\033[m '''))
                if(novo_registro == 2):
                    sleep(1)
                    break
                elif(novo_registro == 1):
                    print()
                else:
                    print('\033[91mOPÇÂO INVALIDA! VOLTANDO AO MENU!\033[m')
            else:
                print('\033[91mNOME DE USUARIO JÁ CADASTRADO \033[m. \033[94mEscolha outro \033[m.')

    elif(opcaoM == 0):
        sleep(1)
        desejo = input('\033[94mDeseja sair do CINE Sertão?\033[m \033[1:7:93:40m[S|N]\033[m: ').upper()
        if(desejo == 'S'):
            print('\033[1:3:7:30:97m[Fechando o CINE Sertão]\033[m', end='')
            (sleep(1))
            print('\033[93:42m ° \033[m', end='')
            (sleep(1))
            print('\033[91:43m ° \033[m', end='')
            (sleep(1))
            print('\033[92:41m ° \033[m', end='')
            (sleep(1))
            print(f'\033[7:30:41m[ENCERRADO]\033[m')
            break
        elif(desejo == 'N'):
            print('Voltando ao MENU!')
            sleep(1)
        else:
            print('\033[91mOPÇÃO INVÁLIDA!\033[m')
            sleep(1)
    else:
        sleep(1)
        print('\033[91mOPÇÃO INVÁLIDA!\033[m')
