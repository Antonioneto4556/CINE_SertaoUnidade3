import os

def cadastrar_filme(filmes, salas_disponiveis):
    titulo = input("Digite o titulo do filme: ")
    if any(filme["titulo"].lower() == titulo.lower() for filme in filmes):
        print("Este filme ja esta cadastrado.")
        return None

    diretor = input("Digite o nome do diretor do filme: ")
    data_estreia = input("Digite a data de estreia do filme (DD/MM/AAAA): ")
    horario_exibicao = input("Digite o horario de exibicao do filme (HH:MM): ")
    valor_ingresso = float(input("Digite o valor do ingresso do filme: "))
    generos = input("Digite os generos do filme (separados por virgulas): ").split(',')
    classificacao_indicativa = int(input("Digite a classificacao indicativa do filme: "))

    if not salas_disponiveis:
        print("Nao ha salas disponiveis para exibir o filme.")
        return None

    print("Salas disponiveis:")
    for i, sala in enumerate(salas_disponiveis):
        print(f"{i + 1}: {sala}")

    while True:
        try:
            sala_index = int(input("Escolha o numero da sala de exibicao: ")) - 1
            if sala_index < 0 or sala_index >= len(salas_disponiveis):
                raise IndexError
            sala = salas_disponiveis[sala_index]
            break
        except (ValueError, IndexError):
            print("Escolha invalida. Tente novamente.")

    capacidade_sala = int(input("Digite a capacidade da sala: "))

    filme = {
        "titulo": titulo,
        "diretor": diretor,
        "data_estreia": data_estreia,
        "horario_exibicao": horario_exibicao,
        "valor_ingresso": valor_ingresso,
        "sala": sala,
        "capacidade_sala": capacidade_sala,
        "generos": [g.strip() for g in generos],
        "classificacao_indicativa": classificacao_indicativa,
        "ingressos_vendidos": 0,
        "acentos_disponiveis": list(range(1, capacidade_sala + 1))
    }

    filmes.append(filme)
    salas_disponiveis.pop(sala_index)

    print(f"Filme '{titulo}' cadastrado com sucesso!")

    # Salvar o filme em um arquivo (exemplo)
    with open("filmes.txt", "a") as arquivo:
        arquivo.write(f"Novo Filme Cadastrado: {titulo}\n")
        arquivo.write(f"Diretor: {diretor}\n")
        arquivo.write(f"Data de Estreia: {data_estreia}\n")
        arquivo.write(f"Horario de Exibicao: {horario_exibicao}\n")
        arquivo.write(f"Valor do Ingresso: {valor_ingresso}\n")
        arquivo.write(f"Sala: {sala}\n")
        arquivo.write(f"Capacidade da Sala: {capacidade_sala}\n")
        arquivo.write(f"Generos: {', '.join(generos)}\n")
        arquivo.write(f"Classificacao Indicativa: {classificacao_indicativa}\n\n")

    return filme
#============================================================================================#


def atualizar_filme(filmes, salas_disponiveis):
    busca = input("Digite o nome do filme ou parte dele: ")
    resultados = [filme for filme in filmes if busca.lower() in filme["titulo"].lower()]
    if resultados:
        print("Filmes encontrados:")
        for i, filme in enumerate(resultados):
            print(f"{i + 1}: {filme['titulo']}")
        escolha_filme = int(input("Escolha o filme pelo numero: ")) - 1
        if 0 <= escolha_filme < len(resultados):
            filme_index = filmes.index(resultados[escolha_filme])
            filme_escolhido = filmes[filme_index]

            novo_titulo = input(f"Digite o novo titulo do filme (atual: {filme_escolhido['titulo']}): ")
            novo_diretor = input(f"Novo nome do diretor do filme (atual: {filme_escolhido['diretor']}): ")
            nova_data_estreia = input(
                f"Nova data de estreia (atual: {filme_escolhido['data_estreia']}, formato DD/MM/AAAA): ")
            novo_horario_exibicao = input(
                f"Novo horario de exibicao (atual: {filme_escolhido['horario_exibicao']}, formato HH:MM): ")
            novo_valor_ingresso = float(
                input(f"Novo valor do ingresso (atual: R${filme_escolhido['valor_ingresso']}): "))
            novos_generos = input(
                f"Novos generos do filme (atual: {', '.join(filme_escolhido['generos'])}, separados por virgulas): ").split(',')
            nova_classificacao_indicativa = int(
                input(f"Nova classificacao indicativa (atual: {filme_escolhido['classificacao_indicativa']}): "))

            print(f"Salas disponiveis (atual: {filme_escolhido['sala']}):")
            for i, sala in enumerate(salas_disponiveis):
                print(f"{i + 1}: {sala}")
            sala_index = int(input("Escolha o numero da nova sala de exibicao (ou 0 para manter a mesma): ")) - 1
            if sala_index == -1:
                nova_sala = filme_escolhido['sala']
            else:
                nova_sala = salas_disponiveis[sala_index]
                salas_disponiveis.pop(sala_index)

            nova_capacidade_sala = int(
                input(f"Digite a nova capacidade da sala (atual: {filme_escolhido['capacidade_sala']}): "))

            filme_escolhido.update({
                "titulo": novo_titulo,
                "diretor": novo_diretor,
                "data_estreia": nova_data_estreia,
                "horario_exibicao": novo_horario_exibicao,
                "valor_ingresso": novo_valor_ingresso,
                "sala": nova_sala,
                "capacidade_sala": nova_capacidade_sala,
                "generos": [g.strip() for g in novos_generos],
                "classificacao_indicativa": nova_classificacao_indicativa
            })
            print("Dados do filme atualizados com sucesso!")

            # Atualizar o arquivo com as informações atualizadas do filme
            with open("filmes.txt", "w") as arquivo:
                for f in filmes:
                    arquivo.write(f"Novo Filme Cadastrado: {f['titulo']}\n")
                    arquivo.write(f"Diretor: {f['diretor']}\n")
                    arquivo.write(f"Data de Estreia: {f['data_estreia']}\n")
                    arquivo.write(f"Horario de Exibicao: {f['horario_exibicao']}\n")
                    arquivo.write(f"Valor do Ingresso: {f['valor_ingresso']}\n")
                    arquivo.write(f"Sala: {f['sala']}\n")
                    arquivo.write(f"Capacidade da Sala: {f['capacidade_sala']}\n")
                    arquivo.write(f"Generos: {', '.join(f['generos'])}\n")
                    arquivo.write(f"Classificacao Indicativa: {f['classificacao_indicativa']}\n\n")

            return filme_escolhido
    else:
        print("Nenhum filme encontrado com essa busca.")
        return None
# ============================================================================================#


def buscar_filmes(filmes):
    print("Escolha o criterio de busca:")
    print("1: Titulo")
    print("2: Sala")
    opcao = input("Digite o numero correspondente ao criterio de busca: ")

    if opcao == '1':
        criterio_busca = 'titulo'
    elif opcao == '2':
        criterio_busca = 'sala'
    else:
        print("Opcao invalida.")
        return None

    busca = input(f"Digite o {criterio_busca} do filme desejado: ").strip().lower()

    resultados = []

    for filme in filmes:
        if busca in str(filme[criterio_busca]).lower():
            resultados.append(filme)

    if resultados:
        print("Filmes encontrados:")
        for i, filme in enumerate(resultados):
            print(f"{i + 1}: {filme['titulo']}")
        escolha_filme = int(input("Escolha o filme pelo numero: ")) - 1
        if 0 <= escolha_filme < len(resultados):
            filme_escolhido = resultados[escolha_filme]
            print("Detalhes do filme:")
            print(f"Titulo: {filme_escolhido['titulo']}")
            print(f"Diretor: {filme_escolhido['diretor']}")
            print(f"Data de Estreia: {filme_escolhido['data_estreia']}")
            print(f"Horario de Exibicao: {filme_escolhido['horario_exibicao']}")
            print(f"Valor do Ingresso: R${filme_escolhido['valor_ingresso']}")
            print(f"Sala: {filme_escolhido['sala']}")
            print(f"Capacidade da Sala: {filme_escolhido['capacidade_sala']}")
            print(f"Ingressos Vendidos: {filme_escolhido['ingressos_vendidos']}")
            return filme_escolhido
    else:
        print("Nenhum filme encontrado com essa busca.")
        return None
# ============================================================================================#


def remover_filme(filmes, salas_disponiveis):
    titulo = input("Digite o titulo do filme que deseja remover: ").strip().lower()
    for filme in filmes:
        if filme["titulo"].lower() == titulo:
            filmes.remove(filme)
            salas_disponiveis.append(filme["sala"])
            print(f"Filme '{titulo}' removido com sucesso!")
            return
    print(f"Filme '{titulo}' nao encontrado.")
# ============================================================================================#


def listar_filmes(filmes):
    print("Escolha uma opcao:")
    print("[1] Sessao atual")
    print("[2] Armazem de filmes")
    opcao = input("Digite o numero correspondente a opcao desejada: ")

    if opcao == '1':
        print("\nSessao Atual:")
        if filmes:
            for filme in filmes:
                print(f"Titulo: {filme['titulo']}")
                print(f"Diretor: {filme['diretor']}")
                print(f"Data de Estreia: {filme['data_estreia']}")
                print(f"Horario de Exibicao: {filme['horario_exibicao']}")
                print(f"Valor do Ingresso: R${filme['valor_ingresso']}")
                print(f"Sala: {filme['sala']}")
                print(f"Capacidade da Sala: {filme['capacidade_sala']}")
                print(f"Generos: {', '.join(filme['generos'])}")
                print(f"Classificacao Indicativa: {filme['classificacao_indicativa']}")
                print(f"Ingressos Vendidos: {filme['ingressos_vendidos']}")
                print()
        else:
            print("Nenhum filme cadastrado.")

    elif opcao == '2':
        print("\nArmazem de Filmes:")
        try:
            with open("filmes.txt", "r") as arquivo:
                conteudo = arquivo.read()
                print(conteudo)
        except FileNotFoundError:
            print("Arquivo de filmes nao encontrado.")
    else:
        print("Opcao invalida.")
# ============================================================================================#


# cinema/gerenciando_filmes.py

def gerenciar_salas(salas_disponiveis):
    while True:
        print("\nGerenciamento de Salas:")
        print("1: Listar salas disponiveis")
        print("2: Adicionar nova sala")
        print("3: Remover sala")
        print("0: Voltar")
        opcao_sala = input("Escolha uma opcao: ").strip()

        if opcao_sala == '1':
            print("\nSalas disponiveis:")
            for sala in salas_disponiveis:
                print(sala)
        elif opcao_sala == '2':
            nova_sala = input("Digite o nome da nova sala: ").strip()
            if nova_sala in salas_disponiveis:
                print("Sala ja existente.")
            else:
                salas_disponiveis.append(nova_sala)
                print(f"Sala '{nova_sala}' adicionada com sucesso.")
        elif opcao_sala == '3':
            sala_remover = input("Digite o nome da sala a ser removida: ").strip()
            if sala_remover in salas_disponiveis:
                salas_disponiveis.remove(sala_remover)
                print(f"Sala '{sala_remover}' removida com sucesso.")
            else:
                print("Sala nao encontrada.")
        elif opcao_sala == '0':
            break
        else:
            print("Opcao invalida.")
# ============================================================================================#


def gerenciar_generos(filmes, admin_logado):
    if admin_logado:
        print("\nGerenciamento de Generos")
        titulo = input("Digite o titulo do filme que deseja atualizar os generos: ").strip()
        for filme in filmes:
            if filme["titulo"].lower() == titulo.lower():
                while True:
                    print(f"\nGeneros do filme '{filme['titulo']}': {', '.join(filme['generos'])}")
                    print("1: Adicionar Genero")
                    print("2: Remover Genero")
                    print("0: Voltar")
                    escolha_genero = input("Escolha uma opcao: ")

                    if escolha_genero == '1':
                        novo_genero = input("Digite o novo genero a ser adicionado: ").strip()
                        if novo_genero:
                            filme['generos'].append(novo_genero)
                            print(f"Genero '{novo_genero}' adicionado com sucesso!")
                        else:
                            print("Genero invalido.")
                    elif escolha_genero == '2':
                        indice_genero = int(input("Digite o indice do genero a ser removido: ").strip()) - 1
                        if 0 <= indice_genero < len(filme['generos']):
                            genero_removido = filme['generos'].pop(indice_genero)
                            print(f"Genero '{genero_removido}' removido com sucesso!")
                        else:
                            print("Indice de genero invalido.")
                    elif escolha_genero == '0':
                        break
                    else:
                        print("Opcao invalida.")
                break
        else:
            print(f"Filme '{titulo}' nao encontrado.")
    else:
        print("Acesso negado. Faca login como administrador para acessar o gerenciamento de generos.")
# ============================================================================================#


def visualizar_vendas_ingressos(filmes):
    print("\nFilmes Disponiveis para Visualizar Vendas:")
    for i, filme in enumerate(filmes):
        print(f"{i + 1}: {filme['titulo']}")

    escolha_filme = int(input("Escolha o numero do filme que deseja visualizar o historico de vendas: ")) - 1
    if 0 <= escolha_filme < len(filmes):
        filme_escolhido = filmes[escolha_filme]
        filename = f"{filme_escolhido['titulo']}_historico_compras.txt"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                print(f"\nHistorico de vendas para {filme_escolhido['titulo']}:")
                print(f.read())
        else:
            print(f"Historico de vendas para {filme_escolhido['titulo']} nao encontrado.")
    else:
        print("Opcao invalida.")
# ============================================================================================#


def gerar_historico_compras_filme(filmes):
    titulo_filme = input("Digite o titulo do filme para ver o historico de compras: ").strip().lower()
    resultados = []

    for filme in filmes:
        if titulo_filme in filme["titulo"].lower():
            resultados.append(filme)

    if resultados:
        print("\nFilmes encontrados:")
        for i, filme in enumerate(resultados):
            print(f"{i + 1}: {filme['titulo']}")

        escolha_filme = int(input("Escolha o numero do filme desejado: ")) - 1
        if 0 <= escolha_filme < len(resultados):
            filme_escolhido = resultados[escolha_filme]
            filename = f"{filme_escolhido['titulo'].replace(' ', '_')}_historico_compras.txt"
            with open(filename, 'w') as f:
                f.write(f"Informacoes do Filme:\n")
                for chave, valor in filme_escolhido.items():
                    f.write(f"{chave.capitalize()}: {valor}\n")
                f.write("\nHistorico de Vendas de Ingressos:\n")
                historico_vendas = f"Historico de vendas para {filme_escolhido['titulo']}:\n"
                if os.path.exists(filename):
                    with open(filename, 'r') as f_leitura:
                        historico_vendas += f_leitura.read()
                else:
                    historico_vendas += "Nenhuma venda registrada ate o momento."
                f.write(historico_vendas)
            print(f"Historico de compras para '{filme_escolhido['titulo']}' salvo com sucesso.")
    else:
        print(f"Nenhum filme encontrado com o titulo '{titulo_filme}'.")
# ============================================================================================#