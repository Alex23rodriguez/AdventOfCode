# %% imports
import sys

sys.path.append("../..")
from itertools import combinations
from pathlib import Path
from pprint import pprint

from grid_utils import get_adjacent, grow
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
# %%
areas = {}
past = set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) in past:
            continue
        new_area = grow(grid, (i, j), lambda x: x==grid[i][j])
        areas[i, j] = new_area
        past.update(new_area)
# %%
perimeters = {}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        perimeters[i, j] = 4 - len(list(get_adjacent(grid, (i, j), diag=False, criteria=lambda x: x==grid[i][j],)))

# %%
ans = {}
for c, v in areas.items():
    ans[c] = len(v) * sum(perimeters[c2] for c2 in v)
# %%
sum(ans.values())
# %%
# %% PART 2
# %%
def is_corner(c1, c2):
    """
    True if c1 __
               c2

    False if  c1 __ c2
    """
    return abs(c1[0] - c2[0]) == 1

def is_concave_corner(grid, cm, c1, c2):
    """
    True if    c1 cm == A A
               __ c2    X A

    False if   c1 cm == A A
               __ c2    A A
    """
    (i, j), (i1, j1), (i2, j2) = cm, c1, c2

    oi = i1 if i1 != i else i2
    oj = j1 if j1 != j else j2
    return grid[oi][oj] != grid[i][j]
    

def count_corners(grid, c):
    i, j = c
    adj = list(a[0] for a in get_adjacent(grid, c, diag=False, criteria=lambda x: x==grid[i][j]))
    if len(adj) == 0: 
        # area of 1 has 4 convex corners
        return 4
    
    elif len(adj) == 1:
        # has 2 convex corners
        return 2
    
    elif len(adj) == 2:
        print('2 adj')
        c1, c2 = adj
        # staight: no corners
        if not is_corner(c1, c2):
            return 0

        # L shape: 1 convex corner and 1 potential concave corner
        return 1 + is_concave_corner(grid, c, c1, c2)

    else: # len(adj) == 3 or 4
        # all potential concave corners
        s = 0
        for c1, c2 in combinations(adj, 2):
            if not is_corner(c1, c2):
                continue
            s += is_concave_corner(grid, c, c1, c2)
        return s
# %%
corners = {}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        corners[i, j] = count_corners(grid, (i, j))

# %%
ans = {}
for c, v in areas.items():
    ans[c] = len(v) * sum(corners[c2] for c2 in v)
# %%
sum(ans.values())
