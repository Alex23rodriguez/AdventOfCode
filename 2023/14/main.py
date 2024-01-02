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
def parse_all_lines(lines: list[str]):
    out = [line for line in lines]
    return out


with timed():
    teststart = parse_all_lines(test_lines)
    start = parse_all_lines(input_lines)


### util defenitions
def tilt(grid, direction: str):
    if direction == "E":
        return tilt_east(grid)
    if direction == "W":
        ans = tilt_east([row[::-1] for row in grid])
        return ["".join(row[::-1]) for row in ans]
    if direction == "N":
        ans = tilt_east(list(zip(*grid)))
        return ["".join(a) for a in zip(*ans)]
    if direction == "S":
        ans = tilt_east(list(zip(*grid[::-1])))
        return ["".join(a) for a in zip(*ans)][::-1]


def tilt_east(grid: list[str]) -> list[str]:
    ans = []
    for row in grid:
        row = "".join(row)
        # easy but very inefficient
        while row != (new_row := row.replace(".O", "O.")):
            row = new_row
        ans.append(row)
    return ans


def calc_load(grid):
    ans = 0
    for i, row in enumerate(reversed(grid), 1):
        ans += i * row.count("O")
    return ans


### main
ngrid = tilt(teststart, "N")
calc_load(ngrid)

###
ngrid = tilt(start, "N")
calc_load(ngrid)  # 106990
###

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
