def entrar(usuarios):
    while True:
        print("\033[1:7:93:40m(1) Login Cliente            \033[m")
        print("\033[1:7:93:40m(2) Login Admin              \033[m")
        print("\033[1:7:93:40m(3) Sair do perfil           \033[m")
        print("\033[1:7:93:40m(4) Voltar ao Menu Principal \033[m")
        opcao = input("\033[92mEscolha uma opcao: \033[m")
        print(f"\033[1:7:97:40m Opcao ({opcao}) selecionada \033[m")
        if opcao == '1':
            nome = input("Nome: ")
            senha = input("Senha: ")
            for cliente in usuarios['clientes']:
                if cliente['nome'] == nome and cliente['senha'] == senha:
                    print(f"\033[92mCliente {nome} logado com sucesso.\033[m")
                    return "cliente", cliente
            print("\033[91mNome ou senha incorretos.\033[m")
            return "cliente"

        elif opcao == '2':
            nome = input("Nome: ")
            senha = input("Senha: ")
            for admin in usuarios['admins']:
                if admin['nome'] == nome and admin['senha'] == senha:
                    print(f"\033[92mAdmin {nome} logado com sucesso.\033[m")
                    return "admin", admin
            print("\033[91mNome ou senha incorretos.\033[m")
            return "admin"

        elif opcao == '3':
            return None

        elif opcao == '4':
            break

        else:
            print(f"\033[1:7:91:40m Opcao ({opcao}) invalida    \033[m")
