# %% imports
import sys

sys.path.append("../..")
from collections import defaultdict
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
def parse_all_lines(lines: list[str], func):
    out = [func(line) for line in lines]
    return out


# %% parse input
def parse_line(line: str):
    # TODO
    return list(line.split())


with timed():
    teststart = parse_all_lines(test_lines, parse_line)[0]
    start = parse_all_lines(input_lines, parse_line)[0]

# %% main
def iter(rocks):
    new_rocks = []
    for r in rocks:
        if r == "0":
            new_rocks.append("1")
        elif (l := len(r)) % 2 == 0:
            new_rocks.append(str(int(r[: l // 2])))
            new_rocks.append(str(int(r[l // 2 :])))
        else:
            new_rocks.append(str(int(r) * 2024))
    return new_rocks


# %%
rocks = start
for i in range(25):
    rocks = iter(rocks)

print(len(rocks))
# %%
# %% PART 2
# %%

def better_iter(rocks):
    new_rocks = defaultdict(lambda: 0)
    for k, v in rocks.items():
        sk = str(k)

        if k == 0:
            new_rocks[1] += v

        elif (l := len(sk)) % 2 == 0:
            new_rocks[int(sk[: l // 2])] += v
            new_rocks[int(sk[l // 2 :])] += v

        else:
            new_rocks[2024 * k] += v

    return new_rocks

# %%
rocks = defaultdict(lambda: 0)
for w in input_txt.split():
    rocks[int(w)] += 1

for i in range(75):
    rocks = better_iter(rocks)

print(sum(rocks.values()))
