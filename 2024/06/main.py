# %% imports
import sys
from pprint import pprint

sys.path.append("../..")
import json
import operator as op
import re
from collections import Counter, defaultdict
from functools import cmp_to_key, lru_cache, partial, reduce
from itertools import (accumulate, combinations, combinations_with_replacement,
                       permutations, zip_longest)
from pathlib import Path

from more_itertools import (bucket, chunked, distinct_combinations,
                            distinct_permutations, distribute, locate, sliced,
                            split_at, split_into, split_when, windowed)

from algs import dijkstra, floyd_warshall
from graph_utils import iden_cross
from grid_utils import get_adjacent, get_from_grid, hgrow, vgrow, walk_from
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

dirs = {
    0: (-1, 0),  # up
    1: (0, 1),  # right
    2: (1, 0),  # down
    3: (0, -1),  # left
}
# %%
pos = list(get_from_grid(grid, lambda x: x == "^"))[0][0]
visited = set([pos])
curr_dir = 0

while True:
    print(f"walking {curr_dir} from {pos}")
    walked = [p[0] for p in walk_from(grid, pos, dirs[curr_dir], criteria=lambda x: x != "#")]
    print(walked)
    visited.update(walked)
    pos = walked[-1]
    if list(walk_from(grid, pos, dirs[curr_dir % 4], limit=1)):
        print("hit obstacle")
        curr_dir += 1
        curr_dir %= 4
    else:
        print("exit")
        break

len(visited)


# %%
# %% PART 2
# %%

grid = start


# %% main
def grid_with_obstacle(grid, obs):
    new = [[c for c in g] for g in grid]
    new[obs[0]][obs[1]] = "#"
    return new


# %%
initial_pos = list(get_from_grid(grid, lambda x: x == "^"))[0][0]
ans = set()

for i in range(len(grid)):
    for j in range(len(grid[0])):
        obs = (i, j)
        if obs == initial_pos or grid[i][j] == "#":
            print(f"skipping {obs}")
            continue

        grid2 = grid_with_obstacle(grid, obs)
        pos = initial_pos
        curr_dir = 0
        walls = set([(obs, curr_dir)])

        # modified part 1
        while True:
            walked = list(walk_from(grid2, pos, dirs[curr_dir], criteria=lambda x: x != "#"))
            if walked:
                walked = [p[0] for p in walked]
                pos = walked[-1]
            else:
                curr_dir += 1
                curr_dir %= 4
                continue

            if (pos, curr_dir) in walls:
                print(f"found loop at {obs}")
                ans.add(obs)
                break
            walls.add((pos, curr_dir))

            if list(walk_from(grid2, pos, dirs[curr_dir % 4], limit=1)):
                curr_dir += 1
                curr_dir %= 4
            else:
                break

print(len(ans))
# %%
