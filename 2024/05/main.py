# %% imports
import sys

sys.path.append("../..")
from functools import cmp_to_key
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
def parse_all_lines(txt: str):
    a, b = txt.split("\n\n")
    a = a.split()
    a = [list(map(int, x.split("|"))) for x in a]
    b = b.strip().split()
    b = [list(map(int, y.split(","))) for y in b]
    return a, b


with timed():
    teststart = parse_all_lines(test_txt)
    start = parse_all_lines(input_txt)

# %% main
A, B = start
before = {}
for x, y in A:
    if x not in before:
        before[x] = set()
    before[x].add(y)


# %%
def correct(manual):
    for i in range(len(manual) - 1, 0, -1):
        v = manual[i]
        if v not in before:
            continue
        if before[v].intersection(manual[:i]):
            return False
    return True


# %%
# [correct(b) for b in B]

# %%
ans = 0
for b in B:
    if correct(b):
        ans += b[len(b) // 2]
print(ans)

# %%
# %% PART 2
# %%
incorrect = list(filter(lambda b: not correct(b), B))
# %%


def cmp(x, y):
    if x in before and y in before[x]:
        return -1
    if y in before and x in before[y]:
        return 1
    return 0


# %%
ans = 0
for bad in incorrect:
    b = sorted(bad, key=cmp_to_key(cmp))
    assert correct(b)
    ans += b[len(b) // 2]
    continue

print(ans)
