from collections import deque
from typing import Any, Callable, Iterable

deque

Graph = dict[Any, dict[Any, float]]


def iden_cross(d) -> Graph:
    G = {}
    for i in d:
        G[i] = {}
        for j in d:
            G[i][j] = 1 if j in d[i] else float("inf")
        G[i][i] = 0
    return G


def bfs(init: Any, get_children: Callable[[Any], Iterable[Any]], goal: Any):
    """Breath First Search"""
    if init == goal:
        return ()

    queue: deque[tuple[Any, ...]] = deque([(init,)])
    while True:
        hist = queue.popleft()
        for child in get_children(hist[-1]):
            curr = hist + (child,)
            if child == goal:
                return curr

            queue.append(curr)
