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
    repeat,
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
    set_partitions,
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
    a, b = line.split()
    b = tuple(map(int, b.split(",")))
    return a, b


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)

### main


###
def get_unknown_groups(springs):
    return [tuple(len(x) for x in line.split(".") if x) for line in springs]


def clean_up(springs: list[str]):
    ans = []
    for sp in springs:
        sp = sp.rstrip(".").lstrip(".")
        while ".." in sp:
            sp = sp.replace("..", ".")
        ans.append(sp)

    return ans


##
def ugly_partition(n, p):
    return set(tuple(sum(x) for x in p) for p in set_partitions([1] * n, p))


##
def to_bin(br, gaps, left, right):
    # binary number from broken 1s and gap 0s
    ans = "0" * left
    for i, gap in enumerate(gaps):
        ans += "1" * br[i]
        ans += "0" * gap
    ans += "1" * br[-1]
    ans += "0" * right
    return int(ans, 2), int(ans.replace("0", ".").replace("1", "0").replace(".", "1"), 2)


##


def get_num(s: str, b: tuple[int]):
    num_gaps = len(b) - 1
    leeway = len(s) - (sum(b) + num_gaps)
    if leeway == 0:
        return 1

    and_num = int(s.replace(".", "0").replace("?", "0").replace("#", "1"), 2)  # used to check that every # is covered
    zand_num = int(s.replace(".", "1").replace("?", "0").replace("#", "0"), 2)  # used to check that every . is empty

    ans = 0
    for outlee in range(0, leeway + 1):
        for left in range(0, outlee + 1):
            right = outlee - left
            for gaps in ugly_partition(leeway - outlee + num_gaps, num_gaps):
                num, znum = to_bin(b, gaps, left, right)
                andd, orr = (num & and_num == and_num), (znum & zand_num) == zand_num
                if andd and orr:
                    ans += 1
    return ans


## TEST
springs, broken = zip(*teststart)
springs = clean_up(springs)
###
get_num(springs[1], broken[1])

###
sum(get_num(s, b) for s, b in zip(springs, broken))
## INPUT
springs, broken = zip(*start)
springs = clean_up(springs)
###
sum(get_num(s, b) for s, b in zip(springs, broken))
###
# PART 2
###


def get_num(s: str, b: tuple[int]):
    print(s, b)
    num_gaps = len(b) - 1
    leeway = len(s) - (sum(b) + num_gaps)
    if leeway == 0:
        return 1

    and_num = int(s.replace(".", "0").replace("?", "0").replace("#", "1"), 2)  # used to check that every # is covered
    zand_num = int(s.replace(".", "1").replace("?", "0").replace("#", "0"), 2)  # used to check that every . is empty

    ans = 0
    for outlee in range(0, leeway + 1):
        for left in range(0, outlee + 1):
            if "#" in s[:left]:
                break
            right = outlee - left
            if "#" in s[len(s) - right :]:
                continue
            for gaps in ugly_partition(leeway - outlee + num_gaps, num_gaps):
                num, znum = to_bin(b, gaps, left, right)
                andd, orr = (num & and_num == and_num), (znum & zand_num) == zand_num
                if andd and orr:
                    ans += 1
    return ans


##
@lru_cache(1024)
def ugly_partition(n, p):
    return set(tuple(sum(x) for x in p) for p in set_partitions([1] * n, p))


## TEST
springs, broken = zip(*teststart)
springs = clean_up(springs)
###
springs2 = ["?".join([s] * 5) for s in springs]
broken2 = [b * 5 for b in broken]
###
with timed():
    sum(get_num(s, b) for s, b in zip(springs2, broken2))
###

with timed():
    print(sum(get_num(s, b) for s, b in zip(springs, broken)))
