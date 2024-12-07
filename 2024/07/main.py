# %% imports
import sys

sys.path.append("../..")
import operator as op
from itertools import combinations_with_replacement
from pathlib import Path

from more_itertools import distinct_permutations

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
    a, *b = line.split()
    a = int(a.strip(":"))
    b = [int(y) for y in b]
    return [a, b]


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)


# %% main
def test_line(a, b):
    for c in combinations_with_replacement((op.add, op.mul), len(b) - 1):
        for p in distinct_permutations(c):
            t = b[0]
            for o, y in zip(p, b[1:]):
                t = o(t, y)
            if t == a:
                return True
    return False


# %%
ans = []
for i, (a, b) in enumerate(start):
    print(i)
    if test_line(a, b):
        ans.append(a)

print(sum(ans))


# %%
# %% PART 2
# %%
def test_line_2(a, b):
    for c in combinations_with_replacement((op.add, op.mul, lambda x, y: int(f"{x}{y}")), len(b) - 1):
        for p in distinct_permutations(c):
            t = b[0]
            for o, y in zip(p, b[1:]):
                t = o(t, y)
            if t == a:
                return True
    return False


# %%
ans = []
for i, (a, b) in enumerate(start):
    print(i)
    if test_line_2(a, b):
        ans.append(a)

print(sum(ans))
