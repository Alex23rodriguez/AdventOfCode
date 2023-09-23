filename = "14.txt"

with open(filename) as f:
    input = f.readlines()

###

paths = [line.replace("\n", "").split(" -> ") for line in input]
paths = [[tuple(map(int, coord.split(","))) for coord in line] for line in paths]

###


def reset():
    global sand, starting
    sand = set()
    for path in paths:
        for coord in path:
            sand.add(coord)

        for a, b in zip(path, path[1:]):
            if a[0] == b[0]:  # vertical
                delta = -1 if a[1] > b[1] else 1
                while a != b:
                    a = (a[0], a[1] + delta)
                    sand.add(a)
            else:
                delta = -1 if a[0] > b[0] else 1
                while a != b:
                    a = (a[0] + delta, a[1])
                    sand.add(a)
    starting = len(sand)


###
reset()

lower = max(s[1] + 1 for s in sand)

while True:
    x, y = 500, 0

    still = False
    while True:
        if (x, y + 1) not in sand:
            y += 1
        elif (x - 1, y + 1) not in sand:
            x, y = x - 1, y + 1
        elif (x + 1, y + 1) not in sand:
            x, y = x + 1, y + 1
        else:
            sand.add((x, y))
            still = True
            break

        if y == lower:
            break
    if not still:
        break

###
print(len(sand) - starting)


### PART 2
reset()

lower = max(s[1] + 2 for s in sand)

while True:
    x, y = 500, 0

    while True:
        if y + 1 == lower:
            sand.add((x, y))
            break

        elif (x, y + 1) not in sand:
            y += 1
        elif (x - 1, y + 1) not in sand:
            x, y = x - 1, y + 1
        elif (x + 1, y + 1) not in sand:
            x, y = x + 1, y + 1
        else:
            sand.add((x, y))
            break

    if (x, y) == (500, 0):
        break


print(len(sand) - starting)
