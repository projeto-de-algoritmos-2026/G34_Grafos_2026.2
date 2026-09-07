from dijkstra import dijkstra_heap, reconstruir_caminho
from enderecos import buscar_enderecos
from visualize import desenhar_rota


def listar_todos(endereco_para_no):
    print("\nEndereços disponíveis:")
    for endereco in sorted(endereco_para_no):
        print(f"  - {endereco}")
    print()


def escolher_endereco(mensagem, endereco_para_no):
    while True:
        query = input(mensagem).strip()

        if query.lower() in ("sair", "exit", "sair()"):
            return None

        if query.lower() in ("listar", "listar endereços", "listar enderecos"):
            listar_todos(endereco_para_no)
            continue

        if not query:
            print("Digite parte de um endereço (ex: 'Acácias') ou 'listar'.")
            continue

        resultados = buscar_enderecos(query, endereco_para_no)

        if not resultados:
            print("Nenhum endereço encontrado com esse texto. "
                  "Tente outro trecho ou digite 'listar' para ver todos.\n")
            continue

        if len(resultados) == 1:
            endereco, no = resultados[0]
            print(f"Endereço encontrado: {endereco}\n")
            return no

        print("\nMais de um endereço encontrado, escolha um pelo número:")
        for idx, (endereco, no) in enumerate(resultados, start=1):
            print(f"  [{idx}] {endereco}")

        escolha = input("Número da opção: ").strip()
        if escolha.isdigit() and 1 <= int(escolha) <= len(resultados):
            endereco, no = resultados[int(escolha) - 1]
            print(f"Selecionado: {endereco}\n")
            return no

        print("Opção inválida, tente novamente.\n")


def executar_modo_interativo(G, no_para_endereco, endereco_para_no):
    print("=" * 60)
    print(" Sistema de Rotas — Bairro Fictício")
    print(" Digite parte de um endereço para buscar (ex: 'Brasil').")
    print(" Digite 'listar' para ver todos os endereços, ou 'sair' para encerrar.")
    print("=" * 60)

    contador_rotas = 0

    while True:
        origem_no = escolher_endereco("\nEndereço de ORIGEM: ", endereco_para_no)
        if origem_no is None:
            break

        destino_no = escolher_endereco("Endereço de DESTINO: ", endereco_para_no)
        if destino_no is None:
            break

        if origem_no == destino_no:
            print("Origem e destino são o mesmo endereço.\n")
            continue

        dist, pred = dijkstra_heap(G, origem_no)
        caminho = reconstruir_caminho(pred, origem_no, destino_no)

        if caminho is None:
            print("Não existe rota possível entre esses dois endereços "
                  "neste cenário (ruas fechadas isolaram a região).\n")
            continue

        print("\nRota encontrada:")
        for no in caminho:
            print(f"  -> {no_para_endereco[no]}")
        print(f"\nTempo total estimado: {dist[destino_no]:.1f} minutos")

        salvar = input("\nSalvar imagem da rota? (s/n): ").strip().lower()
        if salvar == "s":
            contador_rotas += 1
            nome_arquivo = f"rota_{contador_rotas}.png"
            desenhar_rota(G, caminho, origem_no, destino_no,
                          dist[destino_no], nome_arquivo)
            print(f"Imagem salva em {nome_arquivo}")

    print("\nEncerrando. Até a próxima!")
