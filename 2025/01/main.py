# %% imports
import sys

sys.path.append("../..")
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
    # TODO
    return line


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)


# %% main
def part1(start):
    dial = 50
    ans = 0

    for line in start:
        direction, n = line[0], int(line[1:])
        if direction == "L":
            dial -= n
        else:
            dial += n
        dial %= 100
        if dial == 0:
            ans += 1

    print(ans)


# %%
part1(start)


# %%
# %% PART 2
# %%
def part2(start):
    dial = 50
    ans = 0

    for line in start:
        prev = dial
        direction, n = line[0], int(line[1:])
        delta = -1 if direction == "L" else 1

        for _ in range(n):
            dial += delta
            ans += dial % 100 == 0

    print(ans)


# %%
part2(start)
