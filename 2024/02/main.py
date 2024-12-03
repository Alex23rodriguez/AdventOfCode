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


# %% parse input
def parse_line(line: str):
    return list(map(int, line.split()))


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)

# %% main
ans = 0
for l in start:
    if l[0] > l[1]:
        l = list(reversed(l))
    ans += all(1 <= b - a <= 3 for a, b in zip(l, l[1:]))
print(ans)

# %%
# %% PART 2
# %%
p = Path("test2.txt")
if p.exists():
    test_txt = p.read_text()
    test_lines = test_txt.splitlines()


# %% util defenitions
def safe(l):
    return all(1 <= b - a <= 3 for a, b in zip(l, l[1:]))


# %%
# parse input - change parse_line if necessary
# change parse_line if necessary
def parse_line_2(line: str):
    return parse_line(line)


with timed():
    teststart = parse_all_lines(test_lines, parse_line_2)
    start = parse_all_lines(input_lines, parse_line_2)

# %% main
ans = 0
for line in start:
    for l in (line, list(reversed(line))):
        if safe(l):
            ans += 1
            break
        else:
            for i in range(len(l)):
                if safe(l[:i] + l[i + 1 :]):
                    ans += 1
                    break

print(ans)
