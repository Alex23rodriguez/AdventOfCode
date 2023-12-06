### imports
import sys

sys.path.append("../..")
from util import timed
from pathlib import Path

from functools import reduce
import operator as op

### read files
test_txt = Path("test.txt").read_text()
test_lines = test_txt.splitlines()
print(f"read {len((test_lines))} test lines")
input_txt = Path("input.txt").read_text()
input_lines = input_txt.splitlines()
print(f"read {len((input_lines))} lines")


### read functions
def parse_all_lines(lines: list[str]):
    t = list(map(int, lines[0].split()[1:]))
    d = list(map(int, lines[1].split()[1:]))
    return t, d


with timed():
    teststart = parse_all_lines(test_lines)
    start = parse_all_lines(input_lines)

### main
ans = []
for t, d in zip(*teststart):
    a = 0
    for i in range(1, t):
        # print((t-i)*i)
        if (t - i) * i > d:
            a += 1
    ans.append(a)
###
reduce(op.mul, ans)
###
ans = []
for t, d in zip(*start):
    a = 0
    for i in range(1, t):
        # print((t-i)*i)
        if (t - i) * i > d:
            a += 1
    ans.append(a)
###
reduce(op.mul, ans)


###
# PART 2
###
def parse_all_lines(lines: list[str]):
    t = int("".join(lines[0].split()[1:]))
    d = int("".join(lines[1].split()[1:]))
    return t, d


with timed():
    teststart = parse_all_lines(test_lines)
    start = parse_all_lines(input_lines)


### parse input - cange parse_line if necessary
# change parse_line if necessary
### main
t, d = teststart
ans = []
a = 0
for i in range(1, t):
    # print((t-i)*i)
    if (t - i) * i > d:
        a += 1
ans.append(a)
###
reduce(op.mul, ans)
###
with timed():
    t, d = start
    ans = []
    a = 0
    for i in range(1, t):
        # print((t-i)*i)
        if (t - i) * i > d:
            a += 1
    ans.append(a)
    print(reduce(op.mul, ans))
###
