# %% imports
import sys

sys.path.append("../..")
import operator as op
from functools import reduce
from pathlib import Path

from util import timed

# %% read files
test_txt = Path("test.txt").read_text()
test_lines = test_txt.splitlines()
print(f"read {len((test_lines))} test lines")
input_txt = Path("input.txt").read_text()
input_lines = input_txt.splitlines()
print(f"read {len((input_lines))} lines")


# %% read functions
def parse_all_lines(lines: list[str]):
    out = [line.split() for line in lines]
    return out


# %% util defenitions

with timed():
    teststart = parse_all_lines(test_lines)
    start = parse_all_lines(input_lines)

# %% main
op_funcs = {"*": op.mul, "+": op.add}


def part1(st):
    nums, ops = list(zip(*st[:-1])), st[-1]

    ans = [reduce(op_funcs[operation], map(int, col)) for col, operation in zip(nums, ops)]
    print(sum(ans))
    return ans


# %%
part1(start)


# %%
# %% PART 2
# %%
def parse2(lines):
    nums, ops = lines[:-1], lines[-1]
    return nums, ops


teststart = parse2(test_lines)
start = parse2(input_lines)

# %%
nums, ops = teststart


# %%
def part2(st):
    nums, ops = st
    col_indexes = [i for i, v in enumerate(ops) if v != " "]
    ops = [ops[c] for c in col_indexes]

    # split including whitespace
    new_nums = []
    for line in nums:
        new_nums.append([line[c : c2 - 1] for c, c2 in zip(col_indexes, col_indexes[1:])])
        new_nums[-1].append(line[col_indexes[-1] :])

    # zip into columns
    new_nums = list(zip(*new_nums))

    # zip individual chars
    col_nums = [list(zip(*vals)) for vals in new_nums]
    col_nums = [[int("".join(chars)) for chars in num] for num in col_nums]

    ans = [reduce(op_funcs[operation], map(int, col)) for col, operation in zip(col_nums, ops)]
    print(sum(ans))
    return ans


# %%
t = part2(start)
