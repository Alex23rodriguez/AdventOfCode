# imports

###
test_txt = open("test.txt").read()
print(f"read {len(test_txt.splitlines())} test lines")
input_txt = open("input.txt").read()
print(f"read {len(input_txt.splitlines())} lines")


###
# read util functions
def getcoords(xystr):
    x, y = xystr.split(", ")
    return int(x[2:]), int(y[2:])


###
def prepare(inp):
    lines = inp.splitlines()
    out = [line.split("at ")[1:] for line in lines]
    out = [(getcoords(s[0].split(":")[0]), getcoords(s[1].strip())) for s in out]
    return out


teststart = prepare(test_txt)
start = prepare(input_txt)


###
# util functions
def add_interval(loi: list[tuple[int, int]], new: tuple[int, int]):
    """given a list of intervals, append the new one"""
    # append at the end and sort
    fst, *tmp = sorted([*loi, new])
    # merge intervals
    newloi = [fst]
    for x, y in tmp:
        a, b = newloi[-1]
        if b + 1 >= x:
            if y > b:
                newloi[-1] = (a, y)
        else:
            newloi.append((x, y))
    return newloi


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_radius(sensor, beacon, row):
    d = dist(sensor, beacon)
    radius = d - abs(sensor[1] - row)  # how far away the relevant row is

    if radius >= 0:
        return (sensor[0] - radius, sensor[0] + radius)


def count_no_beacon(loi):
    return sum(b - a for a, b in loi)


###
# main
###
# test
loi: list[tuple[int, int]] = []
row = 10
data = teststart
for sensor, beacon in data:
    r = get_radius(sensor, beacon, row)
    print(sensor, beacon)
    if r:
        loi = add_interval(loi, r)
test = count_no_beacon(loi)
check_test()
###
# problem
loi: list[tuple[int, int]] = []
row = 2000000
data = start
radii = []
for sensor, beacon in data:
    r = get_radius(sensor, beacon, row)
    print(sensor, beacon)
    if r:
        radii.append(r)
        print(r)
        loi = add_interval(loi, r)
count_no_beacon(loi)


###
###
# PART 2
def freq(b):
    return b[0] * 4000000 + b[1]


###
for row in range(2000000, 4000001):
    # for row in range(21):
    if row % 100000 == 0:
        print(row)
    loi = []
    for sensor, beacon in data:
        r = get_radius(sensor, beacon, row)
        # print(sensor, beacon)
        if r:
            radii.append(r)
            # print(r)
            loi = add_interval(loi, r)
    if len(loi) == 2:
        print(loi)
        print(freq((loi[0][1] + 1, row)))
        break
print("done")
