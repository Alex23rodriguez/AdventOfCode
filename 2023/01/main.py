### imports
import sys

sys.path.append("../..")
from util import timed

from pathlib import Path

import re

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
pattern = re.compile(r"(\d).*(\d)|(\d)")


### parse input
def parse_line(line: str):
    matches = pattern.search(line)
    assert matches
    a, b, c = matches.groups()
    if not a:
        return int(c + c)
    return int(a + b)


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)

### main
sum(start)

###
# PART 2
###
test_txt = Path("text2.txt").read_text()
test_lines = test_txt.splitlines()

### util defenitions
numsdict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
nums = "|".join(numsdict.keys())

pattern = re.compile(rf"({nums}|\d).*({nums}|\d)|({nums}|\d)")


### parse input
def parse_line_2(line: str):
    matches = pattern.search(line)
    assert matches
    groups = list(matches.groups())
    for i, v in enumerate(groups):
        if v and not v.isdigit():
            groups[i] = numsdict[v]
    a, b, c = groups
    if not a:
        return int(c + c)
    return int(a + b)


with timed():
    teststart = parse_all_lines(test_lines, parse_line_2)
    start = parse_all_lines(input_lines, parse_line_2)
###
sum(start)
