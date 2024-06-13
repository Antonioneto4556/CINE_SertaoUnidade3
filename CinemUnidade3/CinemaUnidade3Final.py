import logando
import cinemenu
import registramento
import pessoas_perfil
import clientela_filmes
import gerenciando_filmes

usuarios = {
    "clientes": [{"nome": "Neto", "senha": "123",
                  "idade": 18, "carteira_estudante": True, "ingressos_comprados": []}],
    "admins": [{"nome": "Antonio", "senha": "neto123"}]
}

filmes = [
    {
        "titulo": "Os Vingadores",
        "diretor": "Joss Whedon",
        "data_estreia": "08/08/2024",
        "horario_exibicao": "18:00",
        "valor_ingresso": 25.00,
        "sala": "Sala 1",
        "capacidade_sala": 10,
        "generos": ["Ação", "Aventura", "Ficção Científica"],
        "classificacao_indicativa": 12,
        "ingressos_vendidos": 0
    },
    {
        "titulo": "Godzilla",
        "diretor": "Japones que não sei o nome",
        "data_estreia": "04/05/2024",
        "horario_exibicao": "18:00",
        "valor_ingresso": 45.00,
        "sala": "Sala 2",
        "capacidade_sala": 100,
        "generos": ["Ação", "Aventura", "Ficção Científica"],
        "classificacao_indicativa": 16,
        "ingressos_vendidos": 0
    }
]

salas_disponiveis = ["Sala 3", "Sala 4", "Sala 5", "Sala 6", ]
cliente_logado = None
admin_logado = None

while True:
    cinemenu.menu_principal()
    escolha = input("\033[1:7:40m ESCOLHA SUA OPÇÃO:          \033[m").strip()

    if escolha == '1':
        if admin_logado:
            while True:
                cinemenu.menu_administrativo()
                sub_opcao = input("Escolha uma opção: ").strip()
                if sub_opcao == '1':
                    gerenciando_filmes.cadastrar_filme(filmes, salas_disponiveis)
                    print("Filme cadastrado com sucesso.")
                elif sub_opcao == '2':
                    gerenciando_filmes.atualizar_filme(filmes, salas_disponiveis)
                    print("Filme atualizado com sucesso.")
                if sub_opcao == '3':
                    gerenciando_filmes.buscar_filmes(filmes)
                    print("Filme selecionado salvo.")
                elif sub_opcao == '4':
                    gerenciando_filmes.remover_filme(filmes, salas_disponiveis)
                    print("Filme removido com sucesso.")
                elif sub_opcao == '5':
                    gerenciando_filmes.listar_filmes(filmes)
                    print("Filmes listados com sucesso.")
                elif sub_opcao == '6':
                    gerenciando_filmes.gerenciar_salas(filmes, salas_disponiveis)
                    print("Sala do filme atualizada com sucesso.")
                elif sub_opcao == '7':
                    gerenciando_filmes.gerenciar_generos(filmes, admin_logado)
                    print("Generos do filme atualizados com sucesso.")
                elif sub_opcao == '8':
                    gerenciando_filmes.visualizar_vendas_ingressos(filmes)
                elif sub_opcao == '9':
                    gerenciando_filmes.gerar_historico_compras_filme(filmes)
                elif sub_opcao == '0':
                    break
                else:
                    print("Opção inválida.")
        else:
            print("Acesso negado. Faça login como administrador para acessar o gerenciamento de filmes.")

    elif escolha == '2':
        clientela_filmes.exibir_filmes_em_cartaz(filmes)

    elif escolha == '3':
        if cliente_logado:
            clientela_filmes.comprar_ingresso(cliente_logado, filmes)
        else:
            print("Você precisa estar logado como cliente para comprar ingressos.")

    elif escolha == '4':
        registramento.cadastro(usuarios, admin_logado)

        elif escolha == '5':
        tipo, usuario_logado = logando.entrar(usuarios)
        if tipo == "cliente":
            cliente_logado = usuario_logado
        elif tipo == "admin":
            admin_logado = usuario_logado
            
    elif escolha == '6':
        if cliente_logado:
            pessoas_perfil.gerenciar_perfil(cliente_logado, filmes)
        else:
            print("Você precisa estar logado como cliente para acessar perfil.")

    elif escolha == '0':
        print("Saindo...")
        break

    else:
        print("\033[91mOpção inválida.\033[m")
