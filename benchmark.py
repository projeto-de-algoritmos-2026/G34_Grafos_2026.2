import time
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from scenario import gerar_bairro
from dijkstra import dijkstra_naive, dijkstra_heap


def medir_tempo(func, graph, origem, repeticoes=3):
    melhores = []
    for _ in range(repeticoes):
        inicio = time.perf_counter()
        func(graph, origem)
        melhores.append(time.perf_counter() - inicio)
    return min(melhores)


def rodar_benchmark(tamanhos):
    resultados_naive = []
    resultados_heap = []
    tamanhos_reais = []

    for lado in tamanhos:
        G = gerar_bairro(linhas=lado, colunas=lado, seed=lado)
        origem = list(G.nodes)[0]

        t_naive = medir_tempo(dijkstra_naive, G, origem)
        t_heap = medir_tempo(dijkstra_heap, G, origem)

        tamanhos_reais.append(G.number_of_nodes())
        resultados_naive.append(t_naive * 1000)  # ms
        resultados_heap.append(t_heap * 1000)

        print(f"n={G.number_of_nodes():>5}  m={G.number_of_edges():>6}  "
              f"naive={t_naive*1000:8.3f} ms   heap={t_heap*1000:8.3f} ms")

    return tamanhos_reais, resultados_naive, resultados_heap


def plotar(tamanhos, naive, heap, caminho_saida):
    plt.figure(figsize=(8, 5.5))
    plt.plot(tamanhos, naive, "o-", label="Versão ingênua O(n²)", color="#d62728")
    plt.plot(tamanhos, heap, "o-", label="Versão com heap O((n+m) log n)", color="#1f77b4")
    plt.xlabel("Número de cruzamentos (n)")
    plt.ylabel("Tempo de execução (ms)")
    plt.title("Dijkstra: ingênuo vs. heap binário")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(caminho_saida, dpi=150)
    plt.close()


if __name__ == "__main__":
    tamanhos = [5, 10, 15, 20, 30, 40, 55, 70]
    n, t_naive, t_heap = rodar_benchmark(tamanhos)
    plotar(n, t_naive, t_heap, "benchmark.png")
