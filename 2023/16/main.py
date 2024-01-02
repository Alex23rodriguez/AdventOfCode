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


### parse input
with timed():
    teststart = test_lines
    start = input_lines


### util defenitions
###
BeamType = tuple[tuple[int, int], tuple[int, int]]

R = (0, 1)
L = (0, -1)
D = (1, 0)
U = (-1, 0)


def move(pos, dir):
    i, j = pos[0] + dir[0], pos[1] + dir[1]
    if i < 0 or j < 0 or i == m or j == n:
        return
    return (i, j), dir


def new_beams(pos, dir, tile) -> list[BeamType]:
    ans = []
    if tile in r"\/":
        if (tile, dir) in [("/", R), ("\\", L)]:
            ans.append(move(pos, U))
        elif (tile, dir) in [("/", L), ("\\", R)]:
            ans.append(move(pos, D))
        elif (tile, dir) in [("/", U), ("\\", D)]:
            ans.append(move(pos, R))
        elif (tile, dir) in [("/", D), ("\\", U)]:
            ans.append(move(pos, L))
    elif tile == "." or (tile == "-" and d in [L, R]) or (tile == "|" and d in [U, D]):
        ans.append(move(pos, dir))
    # split
    elif dir in [L, R]:
        ans.append(move(pos, U))
        ans.append(move(pos, D))
    else:
        ans.append(move(pos, L))
        ans.append(move(pos, R))
    return [beam for beam in ans if beam is not None]


### main
grid = start

m = len(grid)
n = len(grid[0])

beams: list[BeamType] = [((0, 0), R)]
visited: set[BeamType] = set(beams)

while beams:
    p, d = beams.pop()
    nbms = new_beams(p, d, grid[p[0]][p[1]])
    # print("--------")
    # print(p, d)
    # print(nbms)
    for beam in new_beams(p, d, grid[p[0]][p[1]]):
        if beam in visited:
            continue
        visited.add(beam)
        beams.append(beam)

###
len(set(v[0] for v in visited))  # 6740
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
