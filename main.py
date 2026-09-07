from scenario import gerar_bairro
from dijkstra import dijkstra_naive, dijkstra_heap, reconstruir_caminho
from visualize import desenhar_rota
from benchmark import rodar_benchmark, plotar


def main():
    print("=== 1. Gerando o cenário (bairro fictício) ===")
    G = gerar_bairro(linhas=8, colunas=8, seed=7)
    print(f"Cruzamentos: {G.number_of_nodes()}  |  Ruas: {G.number_of_edges()}\n")

    origem = "C0-0"
    destino = "C7-7"

    print(f"=== 2. Calculando rota de menor tempo: {origem} -> {destino} ===")
    dist, pred = dijkstra_heap(G, origem)
    caminho = reconstruir_caminho(pred, origem, destino)

    if caminho is None:
        print("Não há rota possível entre origem e destino neste cenário.")
        return

    print("Caminho encontrado:")
    print(" -> ".join(caminho))
    print(f"Tempo total estimado: {dist[destino]:.1f} minutos\n")

    print("=== 3. Conferindo resultado com a versão ingênua ===")
    dist_naive, _ = dijkstra_naive(G, origem)
    assert abs(dist_naive[destino] - dist[destino]) < 1e-9, "Resultados divergem!"
    print("OK — as duas implementações concordam no custo mínimo.\n")

    print("=== 4. Gerando imagem da rota ===")
    desenhar_rota(G, caminho, origem, destino, dist[destino], "rota.png")
    print("Salvo em rota.png\n")

    print("=== 5. Rodando benchmark ingênuo vs. heap ===")
    tamanhos = [5, 10, 15, 20, 30, 40, 55, 70]
    n, t_naive, t_heap = rodar_benchmark(tamanhos)
    plotar(n, t_naive, t_heap, "benchmark.png")
    print("Salvo em benchmark.png")


if __name__ == "__main__":
    main()
