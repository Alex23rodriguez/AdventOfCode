# %% imports
import sys

import numpy as np

sys.path.append("../..")
import json
import operator as op
import re
from collections import Counter, defaultdict
from copy import deepcopy
from functools import cmp_to_key, lru_cache, partial, reduce
from itertools import (accumulate, combinations, combinations_with_replacement,
                       permutations, zip_longest)
from pathlib import Path
from pprint import pprint

from more_itertools import (bucket, chunked, distinct_combinations,
                            distinct_permutations, distribute, locate, sliced,
                            split_at, split_into, split_when, windowed)

from algs import dijkstra, floyd_warshall
from graph_utils import iden_cross
from grid_utils import get_adjacent, get_from_grid, hgrow, vgrow, walk_from
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
def part1(st):
    most = []
    for line in st:
        i = np.argmax(list(line[:-1]))
        most.append(int(f"{line[i]}{max(line[i + 1 :])}"))

    print(most)
    return sum(most)


part1(start)


# %%


# %%
# %% PART 2
# %%
# def insort(lst: list, val):
#     for i in range(len(lst)):
#         if val > lst[i]:
#             lst.pop(np.argmin(lst[i:]) + i)
#             lst.insert(i, val)
#             return


def insort(lst: list, val):
    lst.insert(0, val)
    for i, (a, b) in enumerate(zip(lst, lst[1:])):
        if a < b:
            lst.pop(i)
            return
    lst.pop()


def part2(st):
    most = []
    for line in st:
        print()
        lst = [int(c) for c in line[-12:]]
        print(lst)
        for c in line[-13::-1]:
            insort(lst, int(c))
            # print(lst)
        most.append(int("".join([str(c) for c in lst])))

    # print(most)
    return sum(most)


part2(start)
