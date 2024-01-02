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
def parse_all_lines(text):
    wfs, ratings = text.split("\n\n")

    wfs = [parse_wf(wf) for wf in wfs.splitlines()]
    wfs = {x: y for x, y in wfs}

    ratings = [parse_rating(r) for r in ratings.splitlines()]

    return wfs, ratings


def parse_rating(rat: str):
    ans = {}
    for pair in rat[1:-1].split(","):
        x, y = pair.split("=")
        ans[x] = int(y)
    return ans


def parse_wf(wf: str):
    ind = wf.index("{")
    k, val = wf[:ind], wf[ind + 1 : -1]
    return k, parse_rule(val)


def parse_rule(val: str):
    rule, res = val.split(":", 1)
    tr, fl = res.split(",", 1)
    if ":" not in fl:
        return rule, tr, fl
    return rule, tr, parse_rule(fl)


with timed():
    teststart = parse_all_lines(test_txt)
    start = parse_all_lines(input_txt)


### util defenitions
def check_accepted(wfs, rating):
    x = rating["x"]
    m = rating["m"]
    a = rating["a"]
    s = rating["s"]

    k = "in"
    while k not in ("R", "A"):
        k = wfs[k]
        while type(k) is tuple:
            k = k[1] if eval(k[0]) else k[2]
    return k == "A"


### main
wfs, ratings = teststart
###
[check_accepted(wfs, r) for r in ratings]
###
sum([sum(r.values()) for r in ratings if check_accepted(wfs, r)])

###
wfs, ratings = start
###
[check_accepted(wfs, r) for r in ratings]
###
sum([sum(r.values()) for r in ratings if check_accepted(wfs, r)])  # 575412

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
