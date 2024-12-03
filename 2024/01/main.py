# %% imports
import sys

sys.path.append("../..")
from collections import Counter
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
    return list(map(int, line.split()))


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)

# %% main
a, b = zip(*start)
ans = [abs(x - y) for x, y in zip(sorted(a), sorted(b))]
print(sum(ans))

# %%
# %% PART 2
# %%
p = Path("test2.txt")
if p.exists():
    test_txt = p.read_text()
    test_lines = test_txt.splitlines()


# %%
### parse input - change parse_line if necessary
# change parse_line if necessary
def parse_line_2(line: str):
    # TODO
    return parse_line(line)


with timed():
    teststart = parse_all_lines(test_lines, parse_line_2)
    start = parse_all_lines(input_lines, parse_line_2)

# %% main
counter_b = Counter(b)
print(sum(x * counter_b[x] for x in a))
