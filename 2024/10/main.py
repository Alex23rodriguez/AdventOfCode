# %% imports
import sys

sys.path.append("../..")
from pathlib import Path

from grid_utils import get_adjacent, get_from_grid
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
    return list(map(int, line))


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)


# %% main
def reachable_from_head(head: tuple[int, int]):
    reachable = set([head])
    n = 1

    while n <= 9 and reachable:
        new_reachable: set[tuple[int, int]] = set()
        for r in reachable:
            new_reachable.update(adj[0] for adj in get_adjacent(grid, r, diag=False, criteria=lambda x: x == n))
        n += 1
        reachable = new_reachable
    return reachable


# %%
grid = start
heads = list(get_from_grid(grid, lambda x: x == 0))

ans = [len(reachable_from_head(h)) for h, _ in heads]
sum(ans)


# %%
# %% PART 2
# %%
def reachable_from_head_rating(head: tuple[int, int]):
    reachable = {head: 1}
    n = 1

    while n <= 9 and reachable:
        new_reachable: dict[tuple[int, int], int] = {}
        for r, rating in reachable.items():
            for adj, _ in get_adjacent(grid, r, diag=False, criteria=lambda x: x == n):
                if adj not in new_reachable:
                    new_reachable[adj] = 0
                new_reachable[adj] += rating
        n += 1
        reachable = new_reachable
    return reachable


# %%
grid = start
heads = list(get_from_grid(grid, lambda x: x == 0))

ans = [sum(reachable_from_head_rating(h).values()) for h, _ in heads]
sum(ans)
