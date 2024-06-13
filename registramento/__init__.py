

def cadastro(usuarios, admin_logado):
    while True:
        print("\nCadastro:")
        print("1: Cadastrar Admin")
        print("2: Cadastrar Cliente")
        print("0: Voltar ao Menu Principal")

        escolha = input("Escolha uma opcao: ")

        if escolha == '1':
            cadastrar_admin(usuarios,admin_logado)
        elif escolha == '2':
            cadastrar_cliente(usuarios)
        elif escolha == '0':
            break
        else:
            print("Opcao invalida.")
# ============================================================================================#


def cadastrar_admin(usuarios, admin_logado):
    if not admin_logado:
        print("Acesso negado. Faca login como administrador.")
        return None

    nome = input("Digite o nome do novo administrador: ").strip()
    senha = input("Digite a senha do novo administrador: ").strip()
    usuarios["admins"].append({"nome": nome, "senha": senha})
    print(f"Administrador '{nome}' cadastrado com sucesso!")
    return {"nome": nome, "senha": senha}
# ============================================================================================#


def cadastrar_cliente(usuarios):
    while True:
        nome = input("Digite seu nome: ").strip()
        nome_existente = any(cliente['nome'] == nome for cliente in usuarios['clientes'])

        if nome_existente:
            print(f"Nome '{nome}' ja esta em uso. Por favor, escolha um nome diferente.")
            continue

        senha = input("Digite sua senha: ").strip()
        idade = int(input("Digite sua idade: "))
        carteira_estudante = input("Possui carteira de estudante? (s/n): ").lower() == 's'

        novo_cliente = {
            "nome": nome,
            "senha": senha,
            "idade": idade,
            "carteira_estudante": carteira_estudante,
            "ingressos_comprados": []
        }

        usuarios["clientes"].append(novo_cliente)
        print(f"Usuario '{nome}' cadastrado com sucesso!")
        return novo_cliente
# ============================================================================================#
