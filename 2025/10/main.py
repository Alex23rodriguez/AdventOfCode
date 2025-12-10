# %% imports
import sys

from tqdm import tqdm

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
from graph_utils import bfs, iden_cross
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
    goal, *buttons, jolt = line.split()
    goal = tuple(c == "#" for c in goal[1:-1])
    buttons = [eval(f"{b[:-1]},)") for b in buttons]
    jolt = eval(f"({jolt[1:-1]})")
    return goal, buttons, jolt


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)


# %% main
def apply(curr: tuple[bool, ...], button):
    return tuple((not c if i in button else c) for i, c in enumerate(curr))


def part1(st):
    ans = []
    for goal, buttons, _ in tqdm(st):
        shortest_path = bfs(
            (False,) * len(goal),
            lambda x: (apply(x, b) for b in buttons),
            goal,
        )
        ans.append(len(shortest_path) - 1)

    return ans


# %%
ans = part1(start)
print(ans)
print(sum(ans))


# %%
# %% PART 2
# %%
def apply2(curr: tuple[int, ...], button):
    return tuple((c + 1 if i in button else c) for i, c in enumerate(curr))


def get_children(goal, buttons, curr):
    # print("curr: ", curr)
    for button in buttons:
        new = apply2(curr, button)
        if all(a <= b for a, b in zip(new, goal)):
            # print(f"applied {button} and yielding {new}")
            yield new
        # print(f"skip applying {button} and yielding {new}")


def part2(st):
    ans = []
    for _, buttons, goal in tqdm(st):
        shortest_path = bfs(
            (0,) * len(goal),
            partial(get_children, goal, buttons),
            goal,
        )
        ans.append(len(shortest_path) - 1)

    return ans


# %%
with timed():
    ans = part2(start)
print(ans)
print(sum(ans))

# %%
_, buttons, goal = teststart[1]
shortest_path = bfs(
    (0,) * len(goal),
    partial(get_children, goal, buttons),
    goal,
)

# %%
pprint(teststart[1])
