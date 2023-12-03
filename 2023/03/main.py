### imports
import sys

sys.path.append("../..")
from util import timed
from pathlib import Path

from grid_utils import get_adjacent, hgrow, get_from_grid


### read files
test_txt = Path("test.txt").read_text()
test_lines = test_txt.splitlines()
print(f"read {len((test_lines))} test lines")
input_txt = Path("input.txt").read_text()
input_lines = input_txt.splitlines()
print(f"read {len((input_lines))} lines")


### util defenitions
def isnum(x):
    return x in "0123456789"


def get_num(grid, coord):
    i, _ = coord
    (_, a), (_, b) = hgrow(grid, coord, isnum)
    return (i, a), int(grid[i][a : b + 1])


### parse input
with timed():
    test_symbols = list(get_from_grid(test_lines, lambda x: x not in ".1234567890"))
    input_symbols = list(get_from_grid(input_lines, lambda x: x not in ".1234567890"))


### main
### TEST
adjnums = []
for coord, _ in test_symbols:
    adjnums.extend(get_adjacent(test_lines, coord, criteria=isnum))

fullnums = set(get_num(test_lines, coord) for coord, _ in adjnums)
print(sum([n for _, n in fullnums]))
### INPUT
adjnums = []
for coord, _ in input_symbols:
    adjnums.extend(get_adjacent(input_lines, coord, criteria=isnum))

fullnums = set(get_num(input_lines, coord) for coord, _ in adjnums)
print(sum([n for _, n in fullnums]))


###
# PART 2
###
### TEST
ratios = []
for coord, sym in test_symbols:
    if sym == "*":
        adjnums = list(get_adjacent(test_lines, coord, criteria=isnum))
        fullnums = set(get_num(test_lines, coord) for coord, _ in adjnums)

        if len(fullnums) == 2:
            a, b = fullnums
            ratios.append(a[1] * b[1])
print(sum(ratios))

### INPUT
ratios = []
for coord, sym in input_symbols:
    if sym == "*":
        adjnums = list(get_adjacent(input_lines, coord, criteria=isnum))
        fullnums = set(get_num(input_lines, coord) for coord, _ in adjnums)

        if len(fullnums) == 2:
            a, b = fullnums
            ratios.append(a[1] * b[1])
print(sum(ratios))
