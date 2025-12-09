# %% imports
import sys

from tqdm import tqdm

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
def parse_all_lines(lines: list[str], func):
    out = [func(line) for line in lines]
    return out


# %% util defenitions


# %% parse input
def parse_line(line: str):
    return list(map(int, line.split(",")))


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)


# %% main
def dist(c1, c2):
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2


def get_dists(st):
    dists = {}
    for i, c1 in tqdm(enumerate(st), total=len(st)):
        for j, c2 in enumerate(st[i + 1 :], i + 1):
            dists[(i, j)] = dist(c1, c2)

    return dists


def part1(st, n):
    dists = get_dists(st)

    sorted_dists = sorted(dists.items(), key=lambda x: x[1])

    circuits: dict[int, tuple] = {i: (i,) for i in range(len(st))}

    for (i, j), _ in sorted_dists[:n]:
        print(i, j)

        if circuits[i] is not circuits[j]:
            new = circuits[i] + circuits[j]
            for ele in circuits[i]:
                circuits[ele] = new
            for ele in circuits[j]:
                circuits[ele] = new

    unique_circuits = set(c for c in circuits.values())

    # return lengths
    return sorted((len(c) for c in unique_circuits), reverse=True)


# %%
lengths = part1(start, 1000)
print(reduce(op.mul, lengths[:3]))


# %%
lengths


# %%
# %% PART 2
# %%
def part2(st):
    dists = get_dists(st)

    sorted_dists = sorted(dists.items(), key=lambda x: x[1])

    circuits: dict[int, tuple] = {i: (i,) for i in range(len(st))}

    for (i, j), _ in sorted_dists:
        print(i, j)

        if circuits[i] is not circuits[j]:
            new = circuits[i] + circuits[j]
            for ele in circuits[i]:
                circuits[ele] = new
            for ele in circuits[j]:
                circuits[ele] = new

            if all(c is circuits[0] for c in circuits.values()):
                return st[i], st[j]

    raise AssertionError


# %%
c1, c2 = part2(start)
print(c1, c2)
print(c1[0] * c2[0])
