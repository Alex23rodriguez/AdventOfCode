import sys

sys.path.append("../..")

from copy import deepcopy
from pprint import pprint

from util import timed

TEST = False

with open("test.txt" if TEST else "input.txt") as f:
    input_str = f.read()
    grid = input_str.splitlines()


# util funcs
def get_adj(coord):
    i, j = coord
    for a, b in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
        if a < 0 or b < 0 or a == len(grid) or b == len(grid[0]):
            continue
        if grid[a][b] == ".":
            yield a, b


### PART 1
# find start
start = None
for i, row in enumerate(grid):
    if "S" in row:
        start = (i, row.index("S"))
        break
assert start


total_steps = 64
first_seen = {start: 0}
step = 0
while step < total_steps:
    new = set()
    for coord, s in first_seen.items():
        if s != step:
            continue
        for c in get_adj(coord):
            if c not in first_seen:
                new.add(c)

    step += 1
    for c in new:
        first_seen[c] = step

# pprint(seen)
print(len([1 for v in first_seen.values() if v % 2 == 0]))


### PART 2
# util funcs
def get(indexable, indexes):
    for i in indexes:
        indexable = indexable[i]
    return indexable


# modify to handle multiple grids
def get_adj2(coord, grid):
    """get adjacent gardens, but also across tiles"""
    m, n = len(grid), len(grid[0])

    I, J, i, j = coord
    for a, b in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
        tmpI = I
        if a < 0:
            tmpI -= 1
        elif a == m:
            tmpI += 1

        tmpJ = J
        if b < 0:
            tmpJ -= 1
        elif b == n:
            tmpJ += 1
        a, b = a % m, b % n

        if grid[a][b] != "#":
            yield tmpI, tmpJ, a, b


###
def print_grid(tile):
    g = [list(row.replace("S", ".")) for row in grid]
    for i, j in tile:
        g[i][j] = "O"
    g = ["".join(row) for row in g]
    pprint(g)


def add_to_graph(before, after, graph):
    # before and after are tile dicts
    for _, tile in before.items():
        if tile in graph:
            assert graph[tile] == after[tile]
        else:
            graph[tile] = after[tile]


def cumulate_per_tile(coords) -> dict[tuple[int, int], list[tuple[int, int]]]:
    ans = {}
    for I, J, i, j in coords:
        if (I, J) not in ans:
            ans[I, J] = []
        ans[I, J].append((i, j))
    return ans


###


def check_diff_repeats(diff):
    return all(x == y for x, y in diff.values())


with timed():
    total_steps = 100

    start_coord = (0, 0, start[0], start[1])
    seen_last_step = {start_coord}
    all_seen = {start_coord}

    new_at_time = {0: frozenset(seen_last_step)}

    cycle_len = len(grid)

    cycle_diff: dict[int, tuple[int, int]] = {i: (0, 0) for i in range(cycle_len)}
    n_seen = {0: 1}

    step = 1

    while True:
        new = set()
        for coord in seen_last_step:
            for c in get_adj2(coord, grid):
                if c not in all_seen:
                    new.add(c)

        # update vars
        all_seen.update(new)

        new_at_time[step] = frozenset(new)

        t = step % (cycle_len)
        n_seen[step] = len(new)

        prev = n_seen.get(step - cycle_len, 0)

        cycle_diff[t] = cycle_diff[t][1], len(new) - prev

        if check_diff_repeats(cycle_diff):
            start_step = step
            # print(f"repeats at step {step}!")
            if step % cycle_len != 0:
                break

        # update condition
        seen_last_step = new
        step += 1

assert start_step
diffs = {i: v[0] for i, v in cycle_diff.items()}
# start_seen =
total_diffs = sum(diffs.values())
print("done!")
###
###
ori_deltas = {}
for k, v in n_seen.items():
    ori_deltas[k % cycle_len] = v


###
def calc_total_at_step(t):
    deltas = ori_deltas.copy()
    ans = 0
    s = t % 2
    while s <= t and s <= start_step:
        ans += n_seen[s]
        s += 2

    for i in range(s, t + 1):
        mod_cyc = i % cycle_len
        deltas[mod_cyc] += diffs[mod_cyc]
        if i % 2 == t % 2:
            ans += deltas[mod_cyc]
    # print(deltas)

    return ans


###
calc_total_at_step(1501)
###
calc_total_at_step(26501365)
###

# 301 should be 80393
# 393 should be 137251
# 394 should be 137941
# 395 should be 138646
# 501 should be 223099 - y
# 511 should be 231968
# 523 should be 242844 - y
# 524 should be 243725 - y
# 525 should be 244644 - n
# 555 should be 273035
# 575 should be 292933
# 597 should be 316632
# 599 should be 318735
# 600 should be 320063
# 601 should be 320862
# 701 should be 435352
# 1501 should be 1994650
###
# 621289877470248 is too low with 26501365 ?
# 621289922886149 is CORRECT
# 621289980339493 is too high with 26501366

# 621336755020852 is too high
