from typing import Any, Callable, Generator


def get_adjacent(
    grid: list,
    coord: tuple[int, int],
    diag=True,
    center=False,
    hwrap=False,
    vwrap=False,
    criteria: Callable[[Any], bool] = lambda _: True,
) -> Generator[tuple[tuple[int, int], Any], None, None]:
    """
    retrieves the (coord, value) pair of all coords adjacent to the given coord.
    note that order is not guaranteed.

    params:
        grid: a 2 dimensional, rectangular
        coord: the initial coordenate
        diag: whether to also include the diagonals default True
        center: whether to also include the given coord. default False
        hwrap: whether to wrap around the edge of the grid horizontally. default False
        vwrap: whether to wrap around the edge of the grid vertically. default False
        criteria: a filter function that the values must satisfy. defaults to all values accepted

    examples:
               12345
        grid = abcde
               ABCDE

        # all defaults
                          234
        coord = (1, 2) -> b d
                          BCD

        coord = (2, 0) -> ab
                           B

        # diag=False
                           3
        coord = (1, 2) -> b d
                           C

        # diag=False, center=True

        coord = (0, 2) -> 234
                           c

        # diag=True, center=True, hwrap=True


        cord = (0, 4) -> 451
                         dea

        # center=True, criteria=lambda x: x.lower() != 'a' and (x not in "12345" or int(x) < 3)

                          12
        coord = (1, 1) ->  bc
                           BC
    """
    i, j = coord
    len_i, len_j = len(grid), len(grid[0])
    assert 0 <= i < len_i, f"{i=} coord outside of range"
    assert 0 <= j < len_j, f"{j=} coord outside of range"

    if diag:
        for i2 in (i - 1, i, i + 1):
            if i2 < 0 or i2 == len_i:
                if not vwrap:
                    continue
                else:
                    i2 = 0 if i2 == len_i else len_i - 1
            for j2 in (j - 1, j, j + 1):
                if j2 < 0 or j2 == len_j:
                    if not hwrap:
                        continue
                    else:
                        j2 = 0 if j2 == len_j else len_j - 1

                if not center and i2 == i and j2 == j:
                    continue
                val = grid[i2][j2]
                if criteria(val):
                    yield (i2, j2), grid[i2][j2]
    else:
        if center:
            yield (i, j), grid[i][j]
        for i2, j2 in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
            if i2 < 0 or i2 == len_i:
                if not vwrap:
                    continue
                else:
                    i2 = 0 if i2 == len_i else len_i - 1
            if j2 < 0 or j2 == len_j:
                if not hwrap:
                    continue
                else:
                    j2 = 0 if j2 == len_j else len_j - 1

            val = grid[i2][j2]
            if criteria(val):
                yield (i2, j2), grid[i2][j2]


def hgrow(
    grid: list,
    coord: tuple[int, int],
    criteria: Callable[[Any], bool],
):
    """given a coordenate, return the the left-right coordenates after expanding horizontally from coord while criteria is True."""
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
    """same as hgrow, but vertical"""
    i, j = coord
    len_i = len(grid)
    assert 0 <= i < len_i, f"{i=} coord outside of range"
    il, ir = i, i
    while il - 1 >= 0 and criteria(grid[il - 1][j]):
        il -= 1
    while ir + 1 < len_i and criteria(grid[ir + 1][j]):
        ir += 1
    return (il, j), (ir, j)


def get_from_grid(grid: list, criteria: Callable[[Any], bool]):
    """retrieve all (coord, val) pairs that fulfill a certain criteria"""
    for i, line in enumerate(grid):
        for j, val in enumerate(line):
            if criteria(val):
                yield (i, j), val


def manhattan_dist(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
