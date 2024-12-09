# %% imports
import sys

sys.path.append("../..")
from itertools import combinations
from pathlib import Path
from pprint import pprint

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


# %% util defenitions


# %% parse input
def parse_line(line: str):
    # TODO
    return line


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)

# %% main
grid = start
txt = input_txt

chars = set(txt)
chars.remove(".")
chars.remove("\n")

antennas = {}
for c in chars:
    antennas[c] = [a[0] for a in get_from_grid(grid, lambda x: x == c)]

pprint(antennas)


# %%
def inbounds(coord, grid):
    return (0 <= coord[0] < len(grid)) and (0 <= coord[1] < len(grid[1]))


# %%
antinodes = set()
for key, coords in antennas.items():
    for (i1, j1), (i2, j2) in combinations(coords, 2):
        di, dj = i1 - i2, j1 - j2
        h1 = i1 + di, j1 + dj
        h2 = i2 - di, j2 - dj

        # print((i1, j1), (i2, j2), h1, h2)
        if inbounds(h1, grid):
            antinodes.add(h1)
        if inbounds(h2, grid):
            antinodes.add(h2)

len(antinodes)


# %%
# %% PART 2
# %%
p = Path("test2.txt")
if p.exists():
    test_txt = p.read_text()
    test_lines = test_txt.splitlines()


# %% util defenitions


# %%
antinodes = set()
for key, coords in antennas.items():
    for (i1, j1), (i2, j2) in combinations(coords, 2):
        di, dj = i1 - i2, j1 - j2
        t = (i1, j1)
        while inbounds(t, grid):
            antinodes.add(t)
            t = t[0] + di, t[1] + dj

        t = (i1, j1)
        while inbounds(t, grid):
            antinodes.add(t)
            t = t[0] - di, t[1] - dj

len(antinodes)
