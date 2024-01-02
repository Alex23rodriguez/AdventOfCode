### imports
import sys

sys.path.append("../..")
from util import timed
from pathlib import Path

import re
import json
from itertools import (
    combinations,
    permutations,
    zip_longest,
    accumulate,
    combinations_with_replacement,
)
from collections import defaultdict, Counter
from functools import reduce, lru_cache, partial, cmp_to_key
import operator as op

from grid_utils import get_adjacent, hgrow, vgrow, get_from_grid
from graph_utils import iden_cross
from algs import dijkstra, floyd_warshall

### read files
test_txt = Path("test.txt").read_text()
test_lines = test_txt.splitlines()
print(f"read {len((test_lines))} test lines")
input_txt = Path("input.txt").read_text()
input_lines = input_txt.splitlines()
print(f"read {len((input_lines))} lines")


### read functions
def parse_all_lines(lines: list[str], func):
    out = [func(line) for line in lines]
    return out


### util defenitions


### parse input
def parse_line(line: str):
    a, b, c = line.split()
    return a, int(b), c.lstrip("(").rstrip(")")


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)

### util
dirs = {
    "R": (0, 1),
    "L": (0, -1),
    "D": (1, 0),
    "U": (-1, 0),
}


def move(pos, dir, n, visited: list):
    i, j = dirs[dir]
    for _ in range(n):
        pos = pos[0] + i, pos[1] + j
        visited.append(pos)
    # pos = pos[0] + i * n, pos[1] + j * n
    return pos


## main
curr = (0, 0)
visited = [curr]

# visited = [curr]
for dir, n, _ in start:
    curr = move(curr, dir, n, visited)
    # verteces.append(curr)

### translate to positive
min_i = min(i for i, _ in visited)
min_j = min(j for _, j in visited)

visited = [(v[0] - min_i, v[1] - min_j) for v in visited]
###
m = max(i for i, _ in visited)
n = max(j for _, j in visited)
grid = [list("." * (n + 1)) for _ in range(m + 1)]
for i, j in visited:
    grid[i][j] = "#"

###
for row in grid:
    print("".join(row))


###
def flood_fill(grid, pos, inside):
    for p in get_adjacent(grid, pos, False, criteria=lambda v: v == "."):
        if p[0] not in inside:
            inside.add(p[0])
            # flood_fill(grid, p[0], inside)


###
startpos = (1, grid[1].index("#") + 1)
inside = set([startpos])
expanded = set()
while to_visit := inside - expanded:
    for p in to_visit:
        expanded.add(p)
        flood_fill(grid, p, inside)
# flood_fill(grid, startpos, inside)
###
###
inside

###
print(len(list(get_from_grid(grid, lambda v: v == "#"))) + len(inside))
# 50603
###
# PART 2
###
p = Path("test2.txt")
if p.exists():
    test_txt = p.read_text()
    test_lines = test_txt.splitlines()


### util defenitions


### parse input - cange parse_line if necessary
# change parse_line if necessary
def parse_line_2(line: str):
    # TODO
    return line


with timed():
    teststart = parse_all_lines(test_lines, parse_line_2)
    start = parse_all_lines(input_lines, parse_line_2)

### main
