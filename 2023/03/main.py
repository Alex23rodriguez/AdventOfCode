### imports
import sys

sys.path.append("../..")
from util import timed

from pathlib import Path


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
def get_num(lines: list[str], i, j):
    jl = j
    jr = j
    while jl - 1 >= 0 and lines[i][jl - 1] in "0123456789":
        jl -= 1
    while jr + 1 < len(lines[0]) and lines[i][jr + 1] in "0123456789":
        jr += 1
    return (i, jl), int(lines[i][jl : jr + 1])


### parse input
def get_sym_coords(lines: list[str]):
    syms = []
    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c not in "0123456789" and c != ".":
                syms.append((i, j))
    return syms


with timed():
    teststart = get_sym_coords(test_lines)
    start = get_sym_coords(input_lines)


### main
def check_sym(lines: list[str], coord, good):
    i, j = coord
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if i + di < 0 or i + di == len(lines) or j + dj < 0 or j + dj == len(lines[0]):
                continue
            c = lines[i + di][j + dj]
            if c in "0123456789":
                good.append(get_num(lines, i + di, j + dj))
    return good


### TEST
good = []
for coord in teststart:
    check_sym(test_lines, coord, good)

good
###
sum(x[1] for x in set(good))
### INPUT
good = []
for coord in start:
    check_sym(input_lines, coord, good)

###
sum(x[1] for x in set(good))


###
# PART 2
###
### TEST

ratios = []
for coord in teststart:
    i, j = coord
    if test_lines[i][j] != "*":
        continue
    nums = set(check_sym(test_lines, coord, []))
    if len(nums) == 2:
        a, b = list(nums)
        ratios.append(a[1] * b[1])
sum(ratios)
###

ratios = []
for coord in start:
    i, j = coord
    if input_lines[i][j] != "*":
        continue
    nums = set(check_sym(input_lines, coord, []))
    if len(nums) == 2:
        a, b = list(nums)
        ratios.append(a[1] * b[1])
sum(ratios)
