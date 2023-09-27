# imports
from itertools import zip_longest
from collections import defaultdict
from datetime import datetime

###
test_txt = open("test.txt").read()

input_txt = open("input.txt").read()
print(f"read {len(input_txt.splitlines())} lines")
###
# read util functions


###
def prepare(inp):
    lines = inp.splitlines()
    out = set(tuple(map(int, l.split(","))) for l in lines)
    return out


teststart = prepare(test_txt)
start = prepare(input_txt)


###
# util functions
def get_bounds(points, padding=0):
    a, b, c = zip(*points)
    return (
        min(a) - padding,
        min(b) - padding,
        min(c) - padding,
    ), (
        max(a) + padding,
        max(b) + padding,
        max(c) + padding,
    )


def count_sa(points):
    xaxis = defaultdict(lambda: [])
    yaxis = defaultdict(lambda: [])
    zaxis = defaultdict(lambda: [])
    for point in points:
        x, y, z = point
        xaxis[(y, z)].append(x)
        yaxis[(x, z)].append(y)
        zaxis[(x, y)].append(z)

    ans = 0
    print()
    for dct in (xaxis, yaxis, zaxis):
        # sort entries
        for k, v in dct.items():
            dct[k] = sorted(v)

        # check if adjecent
        tmp = 0
        for ps in dct.values():
            tmp += 2 * len(ps)  # two sides per axis for every cube
            # subtract adjecent cubes
            tmp -= 2 * sum(p1 + 1 == p2 for p1, p2 in zip(ps, ps[1:]))
        print(f"added {tmp}")
        ans += tmp

    return ans


###
# main
points = start
print("Part 1 ans:", count_sa(points))


###
###
### PART 2
###
###
###
# util fnctions
def check_adjacent(p, neg):
    for axis in range(3):
        for delta in [-1, 1]:
            lst = list(p)
            lst[axis] += delta
            if tuple(lst) in neg:
                return True
    return False


def get_negative(points):
    a, b = get_bounds(points, padding=1)
    added = True
    neg = set([a])
    # could be made more efficient by keeping track of full layers
    # instead of iterating over them each time
    while added:
        added = False
        for x in range(a[0], b[0] + 1):
            for y in range(a[1], b[1] + 1):
                for z in range(a[2], b[2] + 1):
                    p = (x, y, z)
                    if p in neg or p in points:
                        continue
                    # check all 6 sides for outside
                    if check_adjacent(p, neg):
                        neg.add(p)
                        added = True
                        continue
    return neg


def invert_selection(neg):
    points = set()
    a, b = get_bounds(neg, -1)

    for x in range(a[0], b[0] + 1):
        for y in range(a[1], b[1] + 1):
            for z in range(a[2], b[2] + 1):
                p = (x, y, z)
                if p not in neg:
                    points.add(p)
    return points


###

###
now = datetime.now()

points = start
neg = get_negative(points)
print(len(neg))
points2 = invert_selection(neg)
print("Part 2 ans:", count_sa(points2))

print("took", datetime.now() - now)
