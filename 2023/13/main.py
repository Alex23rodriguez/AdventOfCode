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
teststart = [grid.split() for grid in test_txt.split("\n\n")]
start = [grid.split() for grid in input_txt.split("\n\n")]
##


### util
def find_h_mirror(grid: list[str]):
    same = defaultdict(lambda: [])
    pos_starts = []
    for i, row in enumerate(grid):
        same[row].append(i)
        if i - 1 in same[row]:
            pos_starts.append(i)

    # wrong orientation
    if not pos_starts:
        return -1

    for p in pos_starts:
        for a, b in zip(range(p, len(grid)), range(p - 1, -1, -1)):
            if grid[a] != grid[b]:
                break
        else:
            return p

    return -1


def get_val(grid):
    if (p := find_h_mirror(grid)) != -1:
        return 100 * p
    return find_h_mirror(list(zip(*grid)))


## main
ans = [get_val(g) for g in start]
# ans
###
sum(ans)  # 34993


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
