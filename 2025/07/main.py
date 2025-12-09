# %% imports
import sys

sys.path.append("../..")
from collections import defaultdict
from pathlib import Path

from grid_utils import get_from_grid
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
    return line


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)


# %% main
def get_start_and_splitters(st):
    start = next(get_from_grid(st, lambda x: x == "S"))[0][1]

    splitters = {}

    for (i, j), _ in get_from_grid(st, lambda x: x == "^"):
        if i not in splitters:
            splitters[i] = []
        splitters[i].append(j)

    return start, splitters


def part1(st):
    start, splitters = get_start_and_splitters(st)

    num_splits = 0

    beams = set()
    beams.add(start)

    for i in range(max(splitters) + 1):
        if i not in splitters:
            continue

        # start new beams as all untouched beams
        new_beams = beams - set(splitters[i])
        for j in splitters[i]:
            if j in beams:
                new_beams.add(j - 1)
                new_beams.add(j + 1)
                num_splits += 1

        beams = new_beams
        print(i, new_beams)

    print(num_splits)


part1(start)


# %%
# %% PART 2
# %%
def part2(st):
    start, splitters = get_start_and_splitters(st)

    num_splits = 0

    beams = {start: 1}

    for i in range(max(splitters) + 1):
        if i not in splitters:
            continue

        # start new beams as all untouched beams
        new_beams = defaultdict(lambda: 0)
        for b, v in beams.items():
            if b not in splitters[i]:
                new_beams[b] = v

        for j in splitters[i]:
            if j in beams:
                new_beams[j - 1] += beams[j]
                new_beams[j + 1] += beams[j]
        beams = new_beams

        print(i, sum(new_beams.values()))


part2(start)
