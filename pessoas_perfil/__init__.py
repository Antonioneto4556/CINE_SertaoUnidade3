import os


def gerar_boleto(usuario, filmes):
    filename = f"{usuario['nome']}_boleto.txt"
    with open(filename, 'w') as f:
        f.write(f"Boleto para {usuario['nome']}\n")
        f.write("Compras de Ingressos:\n")
        for filme in filmes:
            if 'ingressos' in filme:
                for ingresso in filme['ingressos']:
                    if ingresso['comprador'] == usuario['nome']:
                        f.write(f"Filme: {filme['titulo']}\n")
                        f.write(f"Quantidade: {ingresso['quantidade']}\n")
                        f.write(f"Valor Total: {ingresso['valor_total']}\n")
                        f.write("\n")
    print(f"Boleto gerado em {filename}")
    return filename


def exibir_dados_cliente(cliente_logado):
    print("\n\033[1mInformacoes do Cliente\033[0m")
    print(f"\033[1:7:94:40m {'Nome:':<19}\033[0m\033[1:7:95:40m {cliente_logado['nome']:<30}\033[m")
    print(f"\033[1:7:96:40m {'Idade:':<19}\033[0m\033[1:7:95:40m {cliente_logado['idade']:<30}\033[m")
    print(f"\033[1:7:97:40m {'Carteira Estudante:':<19}\033[0m\033[1:7:95:40m {'Sim'if cliente_logado['carteira_estudante']else'Nao':<30}\033[m")
    ingressos = cliente_logado.get('ingressos_comprados', [])
    print(f"\033[1;34m{'Ingressos Comprados:':<20}\033[0m {len(ingressos):<30}")

    if ingressos:
        print("\033[1mDetalhes dos Ingressos Comprados:\033[0m")
        for ingresso in ingressos:
            print(f"\033[1;34m{'Filme:':<20}\033[0m {ingresso['filme']:<30}")
            print(f"\033[1;34m{'Quantidade:':<20}\033[0m {ingresso['quantidade']:<30}")
            print("\n")


def ver_historico(usuario):
    filename = f"{usuario['nome']}_boleto.txt"
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            print(f"\nHistorico de compras para {usuario['nome']}:")
            print(f.read())
    else:
        print("Nenhum historico de compras encontrado.")


def sair_conta(cliente_logado):
    print(f"Sessao encerrada para {cliente_logado['nome']}.")
    return None


def gerenciar_perfil(cliente_logado, filmes):
    while True:
        print("\nPerfil do Usuario")
        exibir_dados_cliente(cliente_logado)
        print("\033[1:7:94:40m[ 1 ]\033[m\033[7:97:40m Gerar  Boleto \033[m")
        print("\033[1:7:94:40m[ 2 ]\033[m\033[7:97:40m Ver Historico \033[m")
        print("\033[1:7:94:40m[ 3 ]\033[m\033[7:97:40m Sair da Conta \033[m")
        print("\033[1:7:94:40m[ 4 ]\033[m\033[7:97:40m Voltar        \033[m")

        opcao = input("Escolha uma opcao: ")

        if opcao == '1':
            gerar_boleto(cliente_logado, filmes)

        elif opcao == '2':
            ver_historico(cliente_logado)

        elif opcao == '3':
            sair_conta(cliente_logado)
            break

        elif opcao == '4':
            return cliente_logado

        else:
            print("Opcao invalida.")


def salvar_historico_compras(filme):
    filename = f"{filme['titulo']}_historico_compras.txt"
    with open(filename, 'w') as f:
        for ingresso in filme['ingressos']:
            f.write(f"Comprador: {ingresso['comprador']}\n")
            f.write(f"Quantidade: {ingresso['quantidade']}\n")
            f.write(f"Valor Total: {ingresso['valor_total']}\n")
            f.write("\n")
    print(f"\033[94mHistorico de compras salvo em {filename}\033[m")
    return filename


def salvar_ingressos_cliente(cliente):
    nome_arquivo = f"{cliente['nome']}_ingressos.txt"
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write("Ingressos Comprados:\n")
        for ingresso in cliente['ingressos_comprados']:
            arquivo.write(f"Filme: {ingresso['filme']}, Quantidade: {ingresso['quantidade']}\n")
    return nome_arquivo


def visualizar_boleto(cliente):
    nome_arquivo = f"{cliente['nome']}_ingressos.txt"
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
            return conteudo
    except FileNotFoundError:
        print("Nenhum boleto encontrado.")
        return None


def salvar_historico_compras_filme(usuarios, filme):
    nome_arquivo = f"{filme['titulo']}_historico_compras.txt"
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(f"Historico de Compras para o Filme '{filme['titulo']}':\n")
        for cliente in usuarios['clientes']:
            for ingresso in cliente['ingressos_comprados']:
                if ingresso['filme'] == filme['titulo']:
                    arquivo.write(f"Cliente: {cliente['nome']}, Quantidade: {ingresso['quantidade']}\n")
    return nome_arquivo
