### imports
import sys

sys.path.append("../..")
from util import timed
from pathlib import Path
from copy import deepcopy

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

from more_itertools import (
    chunked,
    sliced,
    distribute,
    split_at,
    split_into,
    split_when,
    bucket,
    windowed,
    distinct_permutations,
    distinct_combinations,
    locate,
)

from grid_utils import get_adjacent, hgrow, vgrow, get_from_grid, manhattan_dist
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
    i = 0
    while i < len(lines):
        if "#" not in lines[i]:
            lines.insert(i, lines[i])
            i += 1
        i += 1

    lines = ["".join(ln) for ln in zip(*lines)]

    i = 0
    while i < len(lines):
        if "#" not in lines[i]:
            lines.insert(i, lines[i])
            i += 1
        i += 1

    lines = ["".join(ln) for ln in zip(*lines)]
    return lines


def parse_line(line: str):
    return line


with timed():
    teststart = parse_all_lines(deepcopy(test_lines), parse_line)
    start = parse_all_lines(deepcopy(input_lines), parse_line)

### main
# grid = teststart
grid = start
###
galx = [c for c, _ in get_from_grid(grid, lambda x: x == "#")]
###
ans = []
for x, y in combinations(galx, 2):
    ans.append(manhattan_dist(x, y))
###
sum(ans)


###
# PART 2
###
with timed():
    teststart = deepcopy(test_lines)
    start = deepcopy(input_lines)

### main
grid = start
galx = [c for c, _ in get_from_grid(grid, lambda x: x == "#")]
###
empty_rows = [i for i, ln in enumerate(grid) if "#" not in ln]
empty_cols = [i for i, ln in enumerate(zip(*grid)) if "#" not in ln]


###
def manhattan_dist_mod(c1, c2):
    dist = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
    for r in empty_rows:
        if min(c1[0], c2[0]) < r < max(c1[0], c2[0]):
            dist += 999_999
    for c in empty_cols:
        if min(c1[1], c2[1]) < c < max(c1[1], c2[1]):
            dist += 999_999
    return dist


###

ans = []
for x, y in combinations(galx, 2):
    ans.append(manhattan_dist_mod(x, y))
    # print(x,y, ans[-1])

sum(ans)
