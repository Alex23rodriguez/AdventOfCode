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


###
###
# at, came from
# manually set first directions
## TEST
ts = list(get_from_grid(test_lines, lambda x: x == "S"))[0][0]
grid = teststart
coords = [(add_coords(ts, right), left), (add_coords(ts, down), up)]

## INPUT
ts = list(get_from_grid(input_lines, lambda x: x == "S"))[0][0]
grid = start
coords = [(add_coords(ts, up), down), (add_coords(ts, down), up)]
###
# visited = [(ts, "|")]
visited = {
    (up, down): [ts],
    (left, right): [],
    (up, right): [],
    (left, up): [],
    (left, down): [],
    (right, down): [],
}
ans = 1
while True:
    (c1, p1), (c2, p2) = coords
    if c1 == c2:
        visited[tuple(grid[c1[0]][c1[1]])].append(c1)
        break
    visited[tuple(grid[c1[0]][c1[1]])].append(c1)
    visited[tuple(grid[c2[0]][c2[1]])].append(c2)

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
        print("BREAK")
        break

print(ans)
###


##
## PART 2
##
p = Path("test2.txt")
if p.exists():
    test_txt = p.read_text()
    test_lines = test_txt.splitlines()


##
def pprint(grid):
    for l in grid:
        print("".join(l))


def get(grid, coord):
    return grid[coord[0]][coord[1]]


def insert(grid, coord, val):
    grid[coord[0]][coord[1]] = val


def get_next_dir(grid, coord, prev_dir):
    d1, d2 = get(grid, coord)
    # print(f'{(d1,d2)=}\n{coord=}\n{prev_dir=}')
    if d1 == neg(prev_dir):
        return d2
    assert d2 == neg(prev_dir)
    return d1


def get_new_indir(prev_dir, next_dir, prev_indir):
    if prev_dir == next_dir:
        return prev_indir

    if clockwise[prev_dir] == next_dir:
        return clockwise[prev_indir]

    assert counterclockwise[prev_dir] == next_dir
    return counterclockwise[prev_indir]


##
dirsgrid = start

d = {
    (up, down): "|",
    (left, right): "-",
    (up, right): "L",
    (left, up): "J",
    (left, down): "7",
    (right, down): "F",
}

clockwise = {
    left: down,
    down: right,
    right: up,
    up: left,
}

counterclockwise = {
    left: up,
    up: right,
    right: down,
    down: left,
}
###
from time import sleep

###
grid = [["." for _ in range(len(dirsgrid[0]))] for _ in range(len(dirsgrid))]
for dir, sign in d.items():
    for i, j in visited[dir]:
        grid[i][j] = sign

insert(dirsgrid, ts, (up, down))

curr = (7, 19)  # manually start at upper left corner
startcoord = (7, 20)
prev_dir = left
indir = down
assert get(grid, curr) == "F"

inside = []
failsafe = 0
while curr != startcoord:
    insert(grid, curr, "X")

    if get(grid, add_coords(curr, indir)) == ".":
        inside.append(curr)
        insert(grid, add_coords(curr, indir), "I")

    next_dir = get_next_dir(dirsgrid, curr, prev_dir)
    # redirect indir
    indir = get_new_indir(prev_dir, next_dir, indir)

    # updete curr and came_from
    curr = add_coords(curr, next_dir)
    prev_dir = next_dir

    failsafe += 1
    if failsafe == 15000:
        print("BAD")
        break

print("done!")

pprint(grid)
##

##
incoords = [c for c, _ in get_from_grid(grid, lambda x: x == "I")]
for coord in incoords:
    for adjc, adjv in get_adjacent(grid, coord, diag=False):
        if adjv == ".":
            insert(grid, adjc, "I")


pprint(grid)
print(len(incoords))
###
# 257 - too low
# 270 - too high
# 260 - too low
# 265 - correct!
