from contextlib import contextmanager
from datetime import datetime
from typing import Any, Callable

# types
Graph = dict[Any, dict[Any, float]]


### timing funcs
@contextmanager
def timed():
    start_time = datetime.now()
    yield
    print(f"took {datetime.now() - start_time}")


### grid helpers
def get_adjacent(
    grid: list,
    coord: tuple[int, int],
    diag=True,
    center=False,
):
    i, j = coord
    len_i, len_j = len(grid), len(grid[0])
    assert 0 <= i < len_i, f"{i=} coord outside of range"
    assert 0 <= j < len_j, f"{j=} coord outside of range"

    if diag:
        for i2 in (i - 1, i, i + 1):
            if i2 < 0 or i2 == len_i:
                continue
            for j2 in (j - 1, j, j + 1):
                if j2 < 0 or j2 == len_j:
                    continue
                if not center and i2 == i and j2 == j:
                    continue
                yield (i2, j2), grid[i2][j2]
    else:
        if center:
            yield (i, j), grid[i][j]
        for i2, j2 in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
            if i2 < 0 or i2 == len_i:
                continue
            if j2 < 0 or j2 == len_j:
                continue

            yield (i2, j2), grid[i2][j2]


def hgrow(
    grid: list,
    coord: tuple[int, int],
    criteria: Callable[[Any], bool],
):
    i, j = coord
    line = grid[i]
    len_j = len(grid[0])
    assert 0 <= j < len_j, f"{j=} coord outside of range"
    jl, jr = j, j
    while jl - 1 >= 0 and criteria(line[jl - 1]):
        jl -= 1
    while jr + 1 < len_j and criteria(line[jr + 1]):
        jr += 1
    return (i, jl), (i, jr)


def vgrow(
    grid: list,
    coord: tuple[int, int],
    criteria: Callable[[Any], bool],
):
    i, j = coord
    len_i = len(grid)
    assert 0 <= i < len_i, f"{i=} coord outside of range"
    il, ir = i, i
    while il - 1 >= 0 and criteria(grid[il - 1][j]):
        il -= 1
    while ir + 1 < len_i and criteria(grid[ir + 1][j]):
        ir += 1
    return (il, j), (ir, j)


###
def iden_cross(d) -> Graph:
    G = {}
    for i in d:
        G[i] = {}
        for j in d:
            G[i][j] = 1 if j in d[i] else float("inf")
        G[i][i] = 0
    return G
