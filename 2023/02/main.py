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
def parse_all_lines(lines: list[str], func):
    out = [func(line) for line in lines]
    return out


### util defenitions
colors = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


### parse input
def parse_line(line: str):
    id, txt = line.split(": ")
    id = int(id.split()[1])
    sets = txt.split("; ")
    for s in sets:
        for c in s.split(", "):
            n, col = c.split()
            if colors[col] < int(n):
                return id, False

    return id, True


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)

### main
sum(id for id, poss in teststart if poss)
###

sum(id for id, poss in start if poss)

###
# PART 2
###
p = Path("test2.txt")
if p.exists():
    test_txt = p.read_text()
    test_lines = test_txt.splitlines()


### util defenitions


### parse input - cange parse_line if necessary
# change parse_line if necessary
def parse_line_2(line: str):
    id, txt = line.split(": ")
    id = int(id.split()[1])
    sets = txt.split("; ")
    clrs = []
    for s in sets:
        d = {}
        for c in s.split(", "):
            n, col = c.split()
            d[col] = int(n)
        clrs.append(d)

    return clrs


with timed():
    teststart = parse_all_lines(test_lines, parse_line_2)
    start = parse_all_lines(input_lines, parse_line_2)

### main
mins = []

for clrs in teststart:
    m = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for d in clrs:
        for k, v in d.items():
            m[k] = max(m[k], v)
    mins.append(m)


###
ps = [reduce(op.mul, m.values()) for m in mins]
ps
###
sum(ps)
###
mins = []

for clrs in start:
    m = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for d in clrs:
        for k, v in d.items():
            m[k] = max(m[k], v)
    mins.append(m)


###
ps = [reduce(op.mul, m.values()) for m in mins]
ps
###
sum([reduce(op.mul, m.values()) for m in mins])
