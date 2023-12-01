from contextlib import contextmanager
from datetime import datetime
from typing import Any

# types
Graph = dict[Any, dict[Any, float]]


### timing funcs
@contextmanager
def timed():
    start_time = datetime.now()
    yield
    print(f"took {datetime.now() - start_time}")


###
def iden_cross(d) -> Graph:
    G = {}
    for i in d:
        G[i] = {}
        for j in d:
            G[i][j] = 1 if j in d[i] else float("inf")
        G[i][i] = 0
    return G
