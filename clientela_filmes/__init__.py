import pessoas_perfil

def exibir_filmes_em_cartaz(filmes):
    def truncar(texto, limite):
        if len(texto) <= limite:
            return texto
        else:
            return texto[:limite - 3] + '...'
            
    print(f"\n\033[1:95mFilmes em Cartaz: \033[m")
    print("=--=" * 17)
    print(f"| \033[1:95m{'Titulo':<{20}}\033[m | \033[1:95m{'Diretor':<{15}}\033[m | \033[1:95m{'Generos':<{20}}\033[m |")
    print("=--=" * 17)
    for filme in filmes:
        titulo = truncar(filme['titulo'], 20)
        diretor = truncar(filme['diretor'], 15)
        generos = truncar(', '.join(filme['generos']), 20)
        print(
            f"| \033[94m{titulo:<{20}}\033[m | \033[92m{diretor:<{15}}\033[m | \033[93m{generos:<{20}}\033[m |")
        print("--------------------------------------------------------------------")
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
                return
            quantidade = int(input("Quantos ingressos você deseja comprar? "))
            if quantidade <= 0:
                print("\033[91mQuantidade invalida.\033[m")
                return
            if quantidade > filme_escolhido['capacidade_sala']:
                print("\033[91mQuantidade maior que a capacidade da sala.\033[m")
                return

            total = quantidade * filme_escolhido['valor_ingresso']
            if cliente_logado['carteira_estudante']:
                total *= 0.5
            print(f"Valor total da compra:\033[92m R${total:.2f}\033[m")

            confirma = input("Confirma a compra? (s/n): ").strip().lower()
            if confirma == 's':
                cliente_logado['ingressos_comprados'].append({
                    'filme': filme_escolhido['titulo'],
                    'quantidade': quantidade
                })
                filme_escolhido['ingressos_vendidos'] += quantidade
                filme_escolhido['capacidade_sala'] -= quantidade
                pessoas_perfil.salvar_ingressos_cliente(cliente_logado)
                print("\033[92mCompra realizada com sucesso!\033[m")
            else:
                print("\033[94mCompra cancelada.\033[m")
        else:
            print("\033[91mFilme invalido.\033[m")
    except ValueError:
        print("\033[91mEntrada invalida. Por favor, insira um numero valido.\033[m")
# ============================================================================================#
