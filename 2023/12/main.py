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

# from more_itertools import (
#     chunked,
#     sliced,
#     distribute,
#     split_at,
#     split_into,
#     split_when,
#     bucket,
#     windowed,
#     distinct_permutations,
#     distinct_combinations,
#     locate,
# )
from numpy import argmax

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
def windowed(iterable, n: int):
    for i in range(len(iterable) - n + 1):
        yield iterable[i : i + n]


### parse input
def parse_line(line: str):
    a, b = line.split()
    return a, list(map(int, b.split(",")))


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)


### util
def split_at_possible(s: str, n: int):
    leftovers = []
    for i, w in enumerate(windowed(s, n)):
        # not delimited by '#'
        if i != 0 and s[i - 1] == "#":
            continue
        if i + n != len(s) and s[i + n] == "#":
            continue

        # is possible start point
        if "." not in w:
            leftovers.append((s[: max(0, i - 1)], s[i + n + 1 :]))
    return leftovers


###
def num_fits(s: str, lst: list[int]):
    if len(lst) == 0:
        if "#" in s:
            return 0
        return 1
    # take the max to divide and conquer
    i = argmax(lst)
    x = lst[i]
    left, right = lst[:i], lst[i + 1 :]

    leftovers = split_at_possible(s, x)

    fits = 0
    for l, r in leftovers:
        fits_left = num_fits(l, left)
        if fits_left == 0:
            continue

        fits_right = num_fits(r, right)
        if fits_right == 0:
            continue

        fits += fits_left * fits_right
    return fits


## main
ans = [num_fits(s, lst) for s, lst in teststart]
###
with timed():
    ans = [num_fits(s, lst) for s, lst in start]
###
sum(ans)  # 7260

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
    a, b = line.split()
    return f"{a}.{a}.{a}", list(map(int, b.split(","))) * 3


with timed():
    teststart = parse_all_lines(test_lines, parse_line_2)
    start = parse_all_lines(input_lines, parse_line_2)

### main

with timed():
    ans = [num_fits(s, lst) for s, lst in start]

    print(sum(ans))  # 21374318
