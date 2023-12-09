### imports
import sys

sys.path.append("../..")
from util import timed
from pathlib import Path

from itertools import (
    cycle,
)
from numpy import lcm

###
### read files
test_txt = Path("test.txt").read_text()
test_lines = test_txt.splitlines()
print(f"read {len((test_lines))} test lines")
input_txt = Path("input.txt").read_text()
input_lines = input_txt.splitlines()
print(f"read {len((input_lines))} lines")


### read functions
def parse_all_lines(txt, func):
    dirs, _, *lines = txt.splitlines()
    mp = {}
    for line in lines:
        a, b, c = func(line)
        mp[a] = (b, c)
    return dirs, mp


def parse_line(line: str):
    a, bc = line.split(" = ")
    return a, *bc[1:-1].split(", ")


with timed():
    teststart = parse_all_lines(test_txt, parse_line)
    start = parse_all_lines(input_txt, parse_line)

### main
dirs, mp = teststart
curr = "AAA"
n = 0
for d in cycle(dirs):
    n += 1
    if d == "L":
        curr = mp[curr][0]
    else:
        curr = mp[curr][1]
    if curr == "ZZZ":
        break
print(n)
###

dirs, mp = start
curr = "AAA"
n = 0
for d in cycle(dirs):
    n += 1
    if d == "L":
        curr = mp[curr][0]
    else:
        curr = mp[curr][1]
    if curr == "ZZZ":
        break
print(n)


###
# PART 2
###
### main
p = Path("test2.txt")
if p.exists():
    test_txt = p.read_text()
    test_lines = test_txt.splitlines()
teststart = parse_all_lines(test_txt, parse_line)
###

dirs, mp = teststart
currs = [k for k in mp.keys() if k[-1] == "A"]
## too slow for input!
###


def measure_cycle(dirs, mp, curr):
    ans = {}
    for i, d in enumerate(cycle(dirs), 1):
        # print(curr)
        if d == "L":
            curr = mp[curr][0]
        else:
            curr = mp[curr][1]

        if curr[-1] == "Z":
            if curr not in ans:
                ans[curr] = []

            elif any((i - j) % len(dirs) == 0 for j in ans[curr]):
                break

            ans[curr].append(i)

        # failsafe
        if i > 100_000:
            print("BREAK")
            break
    return ans, (curr, i)


###
measure_cycle(dirs, mp, "11A")
###

[measure_cycle(dirs, mp, c) for c in currs]

###

dirs, mp = start
currs = [k for k in mp.keys() if k[-1] == "A"]
###
currs
###
measure_cycle(dirs, mp, "DNA")
###
cycles = [measure_cycle(dirs, mp, c) for c in currs]
###
cycles

###
# looking at the data, we are able to tell each starting point visits only one endpoint, and they do it every cycle
nums = [list(c[0].values())[0][0] for c in cycles]
###
lcm.reduce(nums)
