from typing import Any

Graph = dict[Any, dict[Any, float]]


def iden_cross(d) -> Graph:
    G = {}
    for i in d:
        G[i] = {}
        for j in d:
            G[i][j] = 1 if j in d[i] else float("inf")
        G[i][i] = 0
    return G
