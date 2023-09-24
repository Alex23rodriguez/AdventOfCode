from copy import deepcopy


###
def dijkstra(G, s):
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


###
def iden_cross(d):
    G = {}
    for i in d:
        G[i] = {}
        for j in d:
            G[i][j] = 1 if j in d[i] else float("inf")
        G[i][i] = 0
    return G


###
def floyd_warshall(G):
    dist = deepcopy(G)
    # KIJ is the correct order
    for k in dist:
        for i in dist:
            for j in dist:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
