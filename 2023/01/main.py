### imports
from contextlib import contextmanager
from datetime import datetime

import re

# import json
# from itertools import (
#     combinations,
#     permutations,
#     zip_longest,
#     accumulate,
#     combinations_with_replacement,
# )
# from collections import defaultdict, Counter
# from functools import reduce, lru_cache, partial
#
# import sys
# sys.path.append('../..')
# import util

### read files
test_txt = open("test.txt").read()
test_lines = test_txt.splitlines()
print(f"read {len((test_lines))} test lines")
input_txt = open("input.txt").read()
input_lines = input_txt.splitlines()
print(f"read {len((input_lines))} lines")

### timing funcs


@contextmanager
def timed():
    start_time = datetime.now()
    yield
    print(f"took {datetime.now() - start_time}")


### read functions
def parse_all_lines(lines: list[str], func):
    out = [func(line) for line in lines]
    return out


###
pattern = re.compile(r"(\d).*(\d)|(\d)")


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
### util functions

### main
sum(start)

###
# PART 2
###
# change parse_line if necessary
test_lines2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()

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
###

pattern = re.compile(rf"({nums}|\d).*({nums}|\d)|({nums}|\d)")


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
    teststart = parse_all_lines(test_lines2, parse_line_2)
    start = parse_all_lines(input_lines, parse_line_2)
###
sum(start)
