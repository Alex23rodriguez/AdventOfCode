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


### parse input
def parse_line(line: str):
    return list(map(int, line.split()))
    return line


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)

### main
seqs = []
for line in teststart:
    ls = [line]
    while any(x != 0 for x in ls[-1]):
        ls.append([y - x for x, y in windowed(ls[-1], 2)])
    seqs.append(ls[:-1])

###
ans = []
for sq in seqs:
    x = sq[-1][0]  # take one from all same row
    for l in reversed(sq[:-1]):
        x += l[-1]

    ans.append(x)
###
sum(ans)

## INPUT
seqs = []
for line in start:
    ls = [line]
    while any(x != 0 for x in ls[-1]):
        ls.append([y - x for x, y in windowed(ls[-1], 2)])
    seqs.append(ls[:-1])

###
ans = []
for sq in seqs:
    x = sq[-1][0]  # take one from all same row
    for l in reversed(sq[:-1]):
        x += l[-1]

    ans.append(x)
###
sum(ans)

###
# PART 2
###
ans = []
for sq in seqs:
    x = sq[-1][0]  # take one from all same row
    for l in reversed(sq[:-1]):
        x = l[0] - x

    ans.append(x)
###
sum(ans)
