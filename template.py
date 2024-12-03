# %% imports
import sys

sys.path.append("../..")
import json
import operator as op
import re
from collections import Counter, defaultdict
from functools import cmp_to_key, lru_cache, partial, reduce
from itertools import (accumulate, combinations, combinations_with_replacement,
                       permutations, zip_longest)
from pathlib import Path

from more_itertools import (bucket, chunked, distinct_combinations,
                            distinct_permutations, distribute, locate, sliced,
                            split_at, split_into, split_when, windowed)

from algs import dijkstra, floyd_warshall
from graph_utils import iden_cross
from grid_utils import get_adjacent, get_from_grid, hgrow, vgrow
from util import timed

# %% read files
test_txt = Path("test.txt").read_text()
test_lines = test_txt.splitlines()
print(f"read {len((test_lines))} test lines")
input_txt = Path("input.txt").read_text()
input_lines = input_txt.splitlines()
print(f"read {len((input_lines))} lines")


# %% read functions
def parse_all_lines(lines: list[str], func):
    out = [func(line) for line in lines]
    return out


# %% util defenitions


# %% parse input
def parse_line(line: str):
    # TODO
    return line


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)

# %% main


# %%
# %% PART 2
# %%
p = Path("test2.txt")
if p.exists():
    test_txt = p.read_text()
    test_lines = test_txt.splitlines()


# %% util defenitions


# %%
# parse input - change parse_line if necessary
# change parse_line if necessary
def parse_line_2(line: str):
    # TODO
    return parse_line(line)


with timed():
    teststart = parse_all_lines(test_lines, parse_line_2)
    start = parse_all_lines(input_lines, parse_line_2)

# %% main
