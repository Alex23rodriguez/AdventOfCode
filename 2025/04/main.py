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


# %% parse input
def parse_line(line: str):
    # TODO
    return list(line)


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)


# %% main
def part1(st) -> list[tuple[int, int]]:
    ans = []
    for (i, j), _ in get_from_grid(st, lambda x: x == "@"):
        if len(list(get_adjacent(st, (i, j), criteria=lambda x: x == "@"))) < 4:
            # print(i, j)
            ans.append((i, j))

    return ans


ans = part1(start)
print(len(ans))


# %%
# %% PART 2
# %%
def part2(st):
    ans = 0
    while True:
        rolls = part1(st)
        if not rolls:
            break

        ans += len(rolls)
        for i, j in rolls:
            st[i][j] = "."

    return ans


# %%
part2(start)
