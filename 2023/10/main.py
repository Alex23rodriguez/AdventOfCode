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
left = (0, -1)
right = (0, 1)
up = (-1, 0)
down = (1, 0)


### parse input
def parse_line(line: str):
    d = {
        ".": [],
        "|": [up, down],
        "-": [left, right],
        "L": [up, right],
        "J": [left, up],
        "7": [left, down],
        "F": [right, down],
        "S": [],
    }
    return [d[c] for c in line]


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)


### main
def add_coords(c1, c2):
    return c1[0] + c2[0], c1[1] + c2[1]


def neg(c):
    return (-c[0], -c[1])


## TEST
ts = list(get_from_grid(test_lines, lambda x: x == "S"))[0][0]
grid = teststart
coords = [(add_coords(ts, right), left), (add_coords(ts, down), up)]

## INPUT
ts = list(get_from_grid(input_lines, lambda x: x == "S"))[0][0]
grid = start
coords = [(add_coords(ts, up), down), (add_coords(ts, down), up)]
###
# at, came from
ans = 1
while True:
    (c1, p1), (c2, p2) = coords
    if c1 == c2:
        break

    ans += 1

    pipe1 = grid[c1[0]][c1[1]]
    if pipe1[0] == p1:
        mv = pipe1[1]
        coords[0] = (add_coords(c1, mv), neg(mv))
    else:
        mv = pipe1[0]
        coords[0] = (add_coords(c1, mv), neg(mv))

    pipe2 = grid[c2[0]][c2[1]]
    if pipe2[0] == p2:
        mv = pipe2[1]
        coords[1] = (add_coords(c2, mv), neg(mv))
    else:
        mv = pipe2[0]
        coords[1] = (add_coords(c2, mv), neg(mv))

    if ans == 10000:
        print("BAD")
        break
print("done!", ans)


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
