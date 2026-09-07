from scenario import gerar_bairro
from enderecos import gerar_enderecos
from interactive import executar_modo_interativo
from dijkstra import dijkstra_naive, dijkstra_heap, reconstruir_caminho
from visualize import desenhar_rota
from benchmark import rodar_benchmark, plotar


def demo_automatica(G, no_para_endereco):
    print("=== Demonstração automática ===")
    origem = list(G.nodes)[0]
    destino = list(G.nodes)[-1]

    dist, pred = dijkstra_heap(G, origem)
    caminho = reconstruir_caminho(pred, origem, destino)

    print(f"De {no_para_endereco[origem]} até {no_para_endereco[destino]}:")
    for no in caminho:
        print(f"  -> {no_para_endereco[no]}")
    print(f"Tempo total estimado: {dist[destino]:.1f} minutos\n")

    dist_naive, _ = dijkstra_naive(G, origem)
    assert abs(dist_naive[destino] - dist[destino]) < 1e-9, "Resultados divergem!"
    print("Conferido: as duas implementações concordam no custo mínimo.\n")

    desenhar_rota(G, caminho, origem, destino, dist[destino], "rota.png")
    print("Imagem salva em rota.png\n")

    print("=== Rodando benchmark busca linear vs. heap ===")
    tamanhos = [5, 10, 15, 20, 30, 40, 55, 70]
    n, t_naive, t_heap = rodar_benchmark(tamanhos)
    plotar(n, t_naive, t_heap, "benchmark.png")
    print("Gráfico salvo em benchmark.png")


def main():
    G = gerar_bairro(linhas=8, colunas=8, seed=7)
    no_para_endereco, endereco_para_no = gerar_enderecos(G)

    print("Bairro fictício gerado.")
    print(f"Cruzamentos: {G.number_of_nodes()}  |  Ruas: {G.number_of_edges()}\n")

    print("Escolha o modo:")
    print("  [1] Interativo — digitar endereços de origem/destino no terminal")
    print("  [2] Demonstração automática + benchmark (gera rota.png e benchmark.png)")
    escolha = input("Opção: ").strip()

    if escolha == "2":
        demo_automatica(G, no_para_endereco)
    else:
        executar_modo_interativo(G, no_para_endereco, endereco_para_no)


if __name__ == "__main__":
    main()
