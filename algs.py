from copy import deepcopy

from graph_utils import Graph


### algs
def dijkstra(G: Graph, s):
    dist = {}
    prev = {}
    queue = []
    for v in G:
        dist[v] = float("inf")
        prev[v] = None
        queue.append(v)
    dist[s] = 0

    while queue:
        (_, u), *queue = queue
        for v in G[u]:
            if v not in queue:
                continue
            alt = dist[u] + G[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist, prev


def floyd_warshall(G: Graph):
    dist = deepcopy(G)
    # KIJ is the correct order
    for k in dist:
        for i in dist:
            for j in dist:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
