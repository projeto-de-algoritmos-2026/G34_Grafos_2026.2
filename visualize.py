import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx


def desenhar_rota(G, caminho, origem, destino, dist_total, caminho_saida):
    pos = nx.get_node_attributes(G, "pos")

    plt.figure(figsize=(9, 8))

    nx.draw_networkx_edges(G, pos, edge_color="#cfcfcf", arrows=True,
                            arrowsize=8, width=1)
    nx.draw_networkx_nodes(G, pos, node_color="#e0e0e0",
                            node_size=260, edgecolors="#999999")
    nx.draw_networkx_labels(G, pos, font_size=6)

    if caminho:
        arestas_rota = list(zip(caminho[:-1], caminho[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=arestas_rota,
                                edge_color="#d62728", width=3, arrows=True,
                                arrowsize=14)
        nx.draw_networkx_nodes(G, pos, nodelist=caminho,
                                node_color="#ffb3b3", node_size=280,
                                edgecolors="#d62728")

    # origem e destino em destaque
    nx.draw_networkx_nodes(G, pos, nodelist=[origem], node_color="#2ca02c",
                            node_size=420, label="Origem")
    nx.draw_networkx_nodes(G, pos, nodelist=[destino], node_color="#1f77b4",
                            node_size=420, label="Destino")

    titulo = f"Rota de menor tempo: {origem} -> {destino}  (custo = {dist_total:.1f} min)"
    plt.title(titulo, fontsize=12)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(caminho_saida, dpi=150)
    plt.close()
