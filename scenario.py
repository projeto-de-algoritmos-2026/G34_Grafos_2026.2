import random
import networkx as nx


def gerar_bairro(linhas=6, colunas=6, seed=42, prob_atalho=0.08, prob_bloqueio=0.05):
    random.seed(seed)
    G = nx.DiGraph()

    def nome(i, j):
        return f"C{i}-{j}"


    for i in range(linhas):
        for j in range(colunas):
            G.add_node(nome(i, j), pos=(j, -i))


    for i in range(linhas):
        for j in range(colunas):
            atual = nome(i, j)

            for di, dj in [(0, 1), (1, 0)]:
                vi, vj = i + di, j + dj
                if vi < linhas and vj < colunas:
                    vizinho = nome(vi, vj)

                    if random.random() < prob_bloqueio:
                        continue


                    tempo = round(random.uniform(1.0, 4.0), 1)

                    G.add_edge(atual, vizinho, weight=tempo)
                    if random.random() > 0.15:
                        tempo_volta = round(tempo + random.uniform(-0.3, 0.5), 1)
                        G.add_edge(vizinho, atual, weight=max(0.5, tempo_volta))


    for i in range(linhas - 1):
        for j in range(colunas - 1):
            if random.random() < prob_atalho:
                a, b = nome(i, j), nome(i + 1, j + 1)
                tempo = round(random.uniform(1.5, 3.0), 1)
                G.add_edge(a, b, weight=tempo)
                G.add_edge(b, a, weight=tempo)


    maior_componente = max(nx.strongly_connected_components(G), key=len)
    G = G.subgraph(maior_componente).copy()

    return G


if __name__ == "__main__":
    g = gerar_bairro()
    print(f"Cruzamentos: {g.number_of_nodes()}")
    print(f"Ruas (arestas): {g.number_of_edges()}")
