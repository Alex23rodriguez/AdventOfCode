# imports

###
test_txt = open("test.txt").read()

input_txt = open("input.txt").read()
print(f"read {len(input_txt.splitlines())} lines")
###
# read util functions


###
def prepare(inp):
    return inp.strip()


teststart = prepare(test_txt)
start = prepare(input_txt)
###
# data
rocks = [
    [
        0b0011110,
    ],
    [
        0b0001000,
        0b0011100,
        0b0001000,
    ],
    [
        0b0011100,
        0b0000100,
        0b0000100,
    ],
    [
        0b0010000,
        0b0010000,
        0b0010000,
        0b0010000,
    ],
    [
        0b0011000,
        0b0011000,
    ],
]


###
# util functions
def pprint(cave: list[int], rock=[], level=0):
    cave = cave.copy()
    for rck in rock:
        if level > 0:
            cave[-level] |= rck
            level -= 1
        else:
            cave.append(rck)

    print()
    for l in reversed(cave):
        bn = str(bin(l))[2:].replace("0", ".").replace("1", "#")
        print(bn.rjust(7, "."))


def push(rock, obstacles, w, seq):
    direction = seq[w % len(seq)]
    if direction == "<":
        rock = push_left(rock, obstacles)
    else:
        rock = push_right(rock, obstacles)
    return rock


def push_left(rock, obstacles=[]):
    if any((0b1000000 & rck) for rck in rock):
        return rock
    new_rock = [rck << 1 for rck in rock]
    if any((rck & lvl) for rck, lvl in zip(new_rock, obstacles)):
        return rock
    return new_rock


def push_right(rock, obstacles=[]):
    if any((0b0000001 & rck) for rck in rock):
        return rock

    new_rock = [rck >> 1 for rck in rock]
    if any((rck & lvl) for rck, lvl in zip(new_rock, obstacles)):
        return rock
    return new_rock


def can_fall(rock, cave, level: int):
    return not any((rck & lvl) for rck, lvl in zip(rock, cave[-level - 1 :]))


def rest(rock, cave, level):
    for rck in rock:
        if level > 0:
            cave[-level] |= rck
            level -= 1
        else:
            cave.append(rck)
    return cave


def spawn_rock(r: int, w: int, seq: str):
    # upon spawning, a rock will be pushed 4 times before being level with the highest point
    rock = rocks[r % len(rocks)]
    for i in range(4):
        rock = push(rock, [], w + i, seq)
    return rock


###
# main


def main(N: int, seq, snd_part=False):
    global seen
    cave = [0b1111111]
    w = 0
    for r in range(N):
        # spawn rock
        rock = spawn_rock(r, w, seq)
        w += 4

        # fall rock
        level = 0
        while can_fall(rock, cave, level):
            level += 1
            rock = push(rock, cave[-level:], w, seq)
            w += 1
        cave = rest(rock, cave, level)
        # guess that a tower repeats every certain amount of steps
        if snd_part and r > 1000:
            key = hash(tuple(cave[-1000:]))
            if key in seen:
                rprev, lnprev = seen[key]
                period = r - rprev
                if (N - r) % period == 0:
                    print(f"height at {N = }")
                    ln = len(cave)
                    deltah = ln - lnprev
                    pending_loops = (N-r)//period
                    h = pending_loops*deltah + ln - 2
                    print(h)
                    return
            else:
                seen[key] = (r, len(cave))
    print(len(cave) - 1)


###
seen = {}
N = 2022
seq = start
main(N, seq)
###
###
### PART 2 ###
###
###
seen = {}
N = 1000000000000
seq = start
main(N, seq, snd_part=True)

###
###
# unit tests
def test_can_fall():
    cave = [
        0b1111111,
        0b1011111,
    ]
    rock = [
        0b0100000,
        0b1100000,
    ]
    assert can_fall(rock, cave, 0)

    cave = [
        0b1111111,
        0b1011111,
    ]
    rock = [
        0b1100000,
        0b0100000,
    ]
    assert not can_fall(rock, cave, 0)
    
    cave = [
        0b1111111,
        0b1001111,
        0b1001111,
        0b1011111,
    ]
    rock = [
        0b0110000,
        0b0100000,
        0b0100000,
    ]
    assert can_fall(rock, cave, 2)
    assert not can_fall(rock, cave, 3)
