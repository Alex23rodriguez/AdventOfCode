# imports
from itertools import zip_longest
from collections import defaultdict

###
test_txt = open("test.txt").read()

input_txt = open("input.txt").read()
print(f"read {len(input_txt.splitlines())} lines")
###
# read util functions


###
def prepare(inp):
    lines = inp.splitlines()
    out = [list(map(int, l.split(","))) for l in lines]
    return out


teststart = prepare(test_txt)
start = prepare(input_txt)


###
# util functions
def get_bounds(points):
    a, b, c = zip(*points)
    return (min(a), min(b), min(c)), (max(a), max(b), max(c))


def count_sa(points):
    a, b = get_bounds(points)

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
get_bounds(teststart)
###
# points = [[1,1,1],[2,1,1], [3,1,1], [5,1,1]]
# points = [[1,1,1], [2,1,1]]#, [3,1,1]]
points = teststart
count_sa(points)
