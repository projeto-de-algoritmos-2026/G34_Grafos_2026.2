import heapq
import math


def dijkstra_naive(graph, source):
    dist = {v: math.inf for v in graph.nodes}
    pred = {v: None for v in graph.nodes}
    dist[source] = 0
    nao_visitados = set(graph.nodes)

    while nao_visitados:
        u = min(nao_visitados, key=lambda v: dist[v])
        nao_visitados.remove(u)

        if dist[u] == math.inf:
            break

        for v in graph.successors(u):
            if v in nao_visitados:
                peso = graph[u][v]["weight"]
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    pred[v] = u

    return dist, pred


def dijkstra_heap(graph, source):
    dist = {v: math.inf for v in graph.nodes}
    pred = {v: None for v in graph.nodes}
    dist[source] = 0

    visitados = set()
    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)

        if u in visitados:
            continue
        visitados.add(u)

        for v in graph.successors(u):
            if v in visitados:
                continue
            peso = graph[u][v]["weight"]
            if d + peso < dist[v]:
                dist[v] = d + peso
                pred[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, pred


def reconstruir_caminho(pred, origem, destino):
    if pred.get(destino) is None and destino != origem:
        return None

    caminho = [destino]
    atual = destino
    while atual != origem:
        atual = pred[atual]
        if atual is None:
            return None
        caminho.append(atual)

    caminho.reverse()
    return caminho
