# %% imports
import sys

sys.path.append("../..")
import json
import operator as op
import re
from collections import Counter, defaultdict
from functools import cmp_to_key, lru_cache, partial, reduce
from itertools import (accumulate, combinations, combinations_with_replacement,
                       permutations, zip_longest)
from pathlib import Path

from more_itertools import (bucket, chunked, distinct_combinations,
                            distinct_permutations, distribute, locate, sliced,
                            split_at, split_into, split_when, windowed)

from algs import dijkstra, floyd_warshall
from graph_utils import iden_cross
from grid_utils import get_adjacent, get_from_grid, hgrow, vgrow, walk_from
from util import timed

# %% read files
test_txt = Path("test.txt").read_text()
test_lines = test_txt.splitlines()
print(f"read {len((test_lines))} test lines")
input_txt = Path("input.txt").read_text()
input_lines = input_txt.splitlines()
print(f"read {len((input_lines))} lines")


# %% read functions
def parse_all_lines(lines: list[str], func):
    out = [func(line) for line in lines]
    return out


# %% util defenitions


# %% parse input
def parse_line(line: str):
    # TODO
    return line


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)

# %% main
grid = start
# %%
xs = list(get_from_grid(grid, lambda x: x == "X"))

# %%
ans = 0
for coord, _ in xs:
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == dj == 0:
                continue
            word = "".join(
                [
                    c[1]
                    for c in walk_from(
                        grid,
                        coord,
                        (di, dj),
                        limit=3,
                    )
                ]
            )
            if word == "MAS":
                ans += 1


print(ans)


# %%
# %% PART 2
# %%
def parse_line_2(line: str):
    # TODO
    return parse_line(line)


with timed():
    teststart = parse_all_lines(test_lines, parse_line_2)
    start = parse_all_lines(input_lines, parse_line_2)

# %% main
grid = start
# %%
centers = list(get_from_grid(grid, lambda x: x == "A"))

# %%
ans = 0
for coord, _ in centers:
    a = list(walk_from(grid, coord, (-1, -1), limit=1))
    b = list(walk_from(grid, coord, (1, 1), limit=1))
    x = list(walk_from(grid, coord, (-1, 1), limit=1))
    y = list(walk_from(grid, coord, (1, -1), limit=1))

    if a and b and x and y:
        if (a[0][1] == "M" and b[0][1] == "S") or (a[0][1] == "S" and b[0][1] == "M"):
            if (x[0][1] == "M" and y[0][1] == "S") or (x[0][1] == "S" and y[0][1] == "M"):
                ans += 1
print(ans)
