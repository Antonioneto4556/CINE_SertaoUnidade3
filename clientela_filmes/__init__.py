import pessoas_perfil

def exibir_filmes_em_cartaz(filmes):
    filmes_ordenados = sorted(filmes, key=lambda x: x['ingressos_vendidos'], reverse=True)

    limite_titulo = 20
    limite_diretor = 15
    limite_generos = 20

    def truncar(texto, limite):
        return texto if len(texto) <= limite else texto[:limite - 3] + '...'

    # Cores ANSI
    CABECALHO = '\033[95m'
    AZUL = '\033[94m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    NEGRITO = '\033[1m'
    RESET = '\033[0m'

    # Exibir apenas os 5 primeiros filmes (os mais populares)
    print(f"\n{CABECALHO}{NEGRITO}Filmes em Cartaz:{RESET}")
    print("=--="*20)
    print(f"| {CABECALHO}{NEGRITO}{'Titulo':<{limite_titulo}}{RESET} | {CABECALHO}{NEGRITO}{'Diretor':<{limite_diretor}}{RESET} | {CABECALHO}{NEGRITO}{'Generos':<{limite_generos}}{RESET} |")
    print("=--="*20)
    for filme in filmes_ordenados[:5]:
        titulo = truncar(filme['titulo'], limite_titulo)
        diretor = truncar(filme['diretor'], limite_diretor)
        generos = truncar(', '.join(filme['generos']), limite_generos)
        print(f"| {AZUL}{titulo:<{limite_titulo}}{RESET} | {VERDE}{diretor:<{limite_diretor}}{RESET} | {AMARELO}{generos:<{limite_generos}}{RESET} |")
    print("---------------------------------------------------------------------")
# ============================================================================================#


def comprar_ingresso(cliente_logado, filmes):
    print("\nFilmes Disponiveis para Compra:")
    for i, filme in enumerate(filmes):
        print(f"{i + 1}: {filme['titulo']}")

    try:
        escolha_filme = int(input("Escolha o numero do filme que deseja comprar ingresso: ")) - 1
        if 0 <= escolha_filme < len(filmes):
            filme_escolhido = filmes[escolha_filme]
            print(f"\nVoce escolheu: {filme_escolhido['titulo']}")
            print(f"Classificacao Indicativa: {filme_escolhido['classificacao_indicativa']}")
            if cliente_logado['idade'] < filme_escolhido['classificacao_indicativa']:
                print("Desculpe, voce nao tem idade suficiente para assistir a este filme.")
            else:
                quantidade = int(input("Quantos ingressos voce deseja comprar? "))
                if quantidade <= 0:
                    print("Quantidade invalida.")
                elif quantidade > filme_escolhido['capacidade_sala']:
                    print("Quantidade maior que a capacidade da sala.")
                else:
                    total = quantidade * filme_escolhido['valor_ingresso']
                    if cliente_logado['carteira_estudante']:
                        total *= 0.5
                    print(f"Valor total da compra: R${total:.2f}")

                    confirma = input("Confirma a compra? (s/n): ").strip().lower()
                    if confirma == 's':
                        cliente_logado['ingressos_comprados'].append({
                            'filme': filme_escolhido['titulo'],
                            'quantidade': quantidade
                        })
                        filme_escolhido['ingressos_vendidos'] += quantidade
                        filme_escolhido['capacidade_sala'] -= quantidade
                        pessoas_perfil.salvar_ingressos_cliente(cliente_logado)
                        print("Compra realizada com sucesso!")
                    else:
                        print("Compra cancelada.")
        else:
            print("Filme invalido.")
    except ValueError:
        print("Entrada invalida. Por favor, insira um numero valido.")
# ============================================================================================#