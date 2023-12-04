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
from functools import reduce, lru_cache, partial
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
def points(s1: set, s2: set):
    ln = len(s1.intersection(s2))
    if ln:
        return 2 ** (ln - 1)
    return 0


### parse input
def parse_line(line: str):
    id_value, sets = line.split(": ")
    id_value = int(id_value.split()[1].strip())

    sets = sets.split(" | ")

    set1 = set(map(int, sets[0].split()))
    set2 = set(map(int, sets[1].split()))

    # Return the parsed values
    return id_value, set1, set2


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)

### main


sum([points(s1, s2) for _, s1, s2 in start])

###
# PART 2
###
p = Path("test2.txt")
if p.exists():
    test_txt = p.read_text()
    test_lines = test_txt.splitlines()


### util defenitions

test_points = [len(s1.intersection(s2)) for _, s1, s2 in teststart]
input_points = [len(s1.intersection(s2)) for _, s1, s2 in start]

### parse input - cange parse_line if necessary
### main
count = {id_value: 1 for id_value, _, _ in teststart}
for i, p in enumerate(test_points):
    print(f"{p=}")
    print(count)
    for j in range(p):
        count[i + j + 2] += count[i + 1]
    print(count)
    # break
###
sum(count.values())
###
count = {id_value: 1 for id_value, _, _ in start}
for i, p in enumerate(input_points):
    for j in range(p):
        count[i + j + 2] += count[i + 1]
    # break
###
sum(count.values())
