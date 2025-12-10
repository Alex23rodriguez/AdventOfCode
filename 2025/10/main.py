# %% imports
import sys

import numpy as np
import sympy as sp
from tqdm import tqdm

sys.path.append("../..")
from itertools import product
from pathlib import Path

from graph_utils import bfs
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
def to_linear_system(buttons, goal):
    ans = []
    for button in buttons:
        ans.append([(1 if i in button else 0) for i in range(len(goal))])
    ans.append(-np.array(goal))
    return np.array(ans).T


def get_max_val(m, goal, col):
    row = m.T[col]
    return min(g for r, g in zip(row, goal) if r)


def get_min_presses(buttons, goal):
    m = to_linear_system(buttons, goal)
    rref, pivots = sp.Matrix(m).rref()
    rref = np.array(rref)
    # print(rref)

    # get free variables
    free = sorted(set(range(len(buttons))) - set(pivots))
    # print(free)

    # sol_matrix is made from the columns of all independent varibles and the bias column
    sol_matrix = rref @ (-np.identity(len(buttons) + 1, dtype=int)[free + [-1]]).T

    valid = []

    # get max value for each free variable
    max_free = [get_max_val(m, goal, f) for f in free]
    # cartesian product of ranges
    possible = product(*[list(range(v + 1)) for v in max_free])
    for p in possible:
        free_vector = np.array(p + (1,))
        sol = sol_matrix @ np.array(free_vector)
        if all(v >= 0 for v in sol) and all(v.denominator == 1 for v in sol):
            valid.append(list(sol) + list(int(v) for v in free_vector[:-1]))

    # return valid

    return min(sum(sol) for sol in valid)


# %%
def part2(st):
    ans = []
    for _, buttons, goal in tqdm(st):
        ans.append(get_min_presses(buttons, goal))
    return ans


# %%
ans = part2(start)
print(ans)
print(sum(ans))
