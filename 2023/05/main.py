### imports
import sys

sys.path.append("../..")
from util import timed
from pathlib import Path

from more_itertools import chunked

### read files
test_txt = Path("test.txt").read_text()
test_lines = test_txt.splitlines()
print(f"read {len((test_lines))} test lines")
input_txt = Path("input.txt").read_text()
input_lines = input_txt.splitlines()
print(f"read {len((input_lines))} lines")


### read functions
def parse_all_lines(txt: str):
    sections = txt.split("\n\n")
    seeds, *sections = sections
    seeds = list(map(lambda x: int(x), seeds.split()[1:]))
    d = {}
    for s in sections:
        sc = s.splitlines()
        k = sc[0].split()[0]
        d[k] = list(map(lambda line: [int(x) for x in line.split()], sc[1:]))

    return seeds, d


with timed():
    teststart = parse_all_lines(test_txt)
    start = parse_all_lines(input_txt)


### util definitions
def linmap(s, vs):
    for v in vs:
        (a, b), (x, y) = v
        if a <= s <= b:
            return x + (s - a)
    return s


### main
## TEST
seeds, d = teststart

newd = []
for _, vs in d.items():
    newd.append([])
    for v in vs:
        a, b, c = v
        newd[-1].append(((b, b + c - 1), (a, a + c - 1)))
locs = []
for s in seeds:
    for vs in newd:
        s = linmap(s, vs)
    locs.append(s)
print(min(locs))
## INPUT
seeds, d = start

newd = []
for _, vs in d.items():
    newd.append([])
    for v in vs:
        a, b, c = v
        newd[-1].append(((b, b + c - 1), (a, a + c - 1)))
locs = []
for s in seeds:
    for vs in newd:
        s = linmap(s, vs)
    locs.append(s)
print(min(locs))
###
# PART 2
###
### util defenitions
seeds, d = teststart
moreseeds = []
for a, b in chunked(seeds, 2):
    moreseeds.extend(range(a, a + b))
##
moreseeds

## TEST
locs = []
for s in moreseeds:
    sid = s
    for vs in newd:
        s = linmap(s, vs)
    locs.append((s, sid))
print(min(locs))
##
s = 82
for vs in newd:
    print(vs)
    s = linmap(s, vs)
    print(s)


## updated version
ranges = []
for vs in newd:
    st = sorted(vs)
    print(st)
    # initial range
    s, d = st[0]
    # range start, range end, delta
    ans = [(s[0], s[1], d[0] - s[0])]  # first element
    for (s1, d1), (s2, d2) in zip(st, st[1:]):
        # not continuous, so add a 0 delta
        if s1[1] + 1 != s2[0]:
            ans.append((s1[1] + 1, s2[0] - 1, 0))
        ans.append((s2[0], s2[1], d2[0] - s2[0]))
    ranges.append(ans)
    print(ranges[-1])
# ranges
##


def move(s, r, rngs):
    a, b, c = rngs[0]
    if s + r <= a:
        # print("too small")
        return [(s, r)]
    if s > rngs[-1][1]:
        # print("too big")
        return [(s, r)]
    # print('in')
    ans = []
    if s < a:
        ans.append((s, a - s))
        r -= a - s
        s = a
    for a, b, c in rngs:
        if a <= s <= b:
            print(a, s, b)
        if b < s:
            continue
        d = min(b - s + 1, r)
        ans.append((s + c, d))
        r -= d
        if r == 0:
            return ans
        s = b + 1
    ans.append((s, r))
    return ans


##
move(30, 100, ranges[0])
##
ranges[0]
##
move(82, 1, ranges[0])

##
end = list(chunked(seeds, 2))
# end = [(79, 4)]
# end = [(82, 1)]
print(end)
for rngs in ranges:
    newend = set()
    for s, r in end:
        newend.update(move(s, r, rngs))
    end = newend
    print(rngs)
    print(end)
##
min(end)


###
teststart


### util definitions
def linmap(s, vs):
    for v in vs:
        (a, b), (x, y) = v
        if a <= s <= b:
            return x + (s - a)
    return s


## INPUT
with timed():
    seeds, d = start
    moreseeds = set()
    for a, b in chunked(seeds, 2):
        moreseeds.update(range(a, a + b))
    print(f"{len(moreseeds)=}")
    locs = []
    for s in moreseeds:
        for vs in newd:
            s = linmap(s, vs)
        locs.append(s)
    print(min(locs))
## TOO SLOW
