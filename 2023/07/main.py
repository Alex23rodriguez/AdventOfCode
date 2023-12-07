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


###
def rank(c):
    return "23456789TJQKA".index(c)


def cmprank(c1, c2):
    r1, r2 = rank(c1), rank(c2)
    if r1 < r2:
        return -1
    if r1 > r2:
        return 1
    return 0


### parse input
def parse_line(line: str):
    h, bid = line.split()
    # hs = sorted(h, reverse=True, key=cmp_to_key(cmprank))
    return Counter(h), int(bid), h


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)


### main
def get_hand(h: Counter):
    st = [c for _, c in h.most_common()]
    if st[0] == 5:  # five of a kind
        return 6
    if st[0] == 4:  # four of a kind
        return 5
    if st[0] == 3:
        if st[1] == 2:  # full house
            return 4
        return 3  # three of a kind
    if st[0] == 2:
        if st[1] == 2:
            return 2
        return 1
    return 0


###


# compare hands function
def cmp(pair1, pair2):
    h1, h2 = pair1[0], pair2[0]
    s1, s2 = get_hand(h1), get_hand(h2)
    if s1 > s2:
        return 1
    if s1 < s2:
        return -1
    for c1, c2 in zip(pair1[2], pair2[2]):
        a = rank(c1)
        b = rank(c2)
        if a > b:
            return 1
        if a < b:
            return -1
    return 0


## TEST
ans = sorted(teststart, key=cmp_to_key(cmp))
sum([i * b for i, (_, b, _) in enumerate(ans, 1)])

## INPUT
ans = sorted(start, key=cmp_to_key(cmp))
sum([i * b for i, (_, b, _) in enumerate(ans, 1)])


###
# PART 2
###
def rank(c):
    return "J23456789TQKA".index(c)


def get_hand(h: Counter):
    st = h.most_common()
    js = h["J"]

    if len(st) == 1:  # five of a kind
        return 6

    # scoot over best cards if J is among them
    (c1, n1), (c2, n2) = st[0], st[1]
    if len(st) == 2:
        if c1 == "J" or c2 == "J":
            return 6
    else:
        (c3, n3) = st[2]
        if c1 == "J":
            c1, n1 = c2, n2
            c2, n2 = c3, n3
        elif c2 == "J":
            c2, n2 = c3, n3

    if n1 + js == 5:  # five of a kind
        return 6
    if n1 + js == 4:  # four of a kind
        return 5
    if n1 + js == 3:
        if n2 == 2:  # full house
            return 4
        return 3  # three of a kind
    if n1 + js == 2:
        if n2 == 2:
            return 2
        return 1
    return 0


## TEST
ans = sorted(teststart, key=cmp_to_key(cmp))
sum([i * b for i, (_, b, _) in enumerate(ans, 1)])

## INPUT
ans = sorted(start, key=cmp_to_key(cmp))
sum([i * b for i, (_, b, _) in enumerate(ans, 1)])
