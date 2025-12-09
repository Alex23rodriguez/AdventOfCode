# %% imports
import math
import sys

from tqdm import tqdm

sys.path.append("../..")
from collections import defaultdict
from itertools import combinations
from pathlib import Path
from pprint import pprint

from more_itertools import windowed

from util import timed

# %% read files
test_txt = Path("test.txt").read_text()
test_lines = test_txt.splitlines()
print(f"read {len((test_lines))} test lines")
input_txt = Path("input.txt").read_text()
input_lines = input_txt.splitlines()
print(f"read {len((input_lines))} lines")


# %% read functions
def parse_all_lines(lines: list[str], func):
    out = [tuple(map(int, line.split(","))) for line in lines]
    return out


# %% parse input
def parse_line(line: str):
    # TODO
    return line


with timed():
    teststart = parse_all_lines(test_lines, parse_line)
    start = parse_all_lines(input_lines, parse_line)


# %% main
def area(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def part1(st):
    return max(area(c1, c2) for c1, c2 in combinations(st, 2))


# %%
part1(start)


# %%
# %% PART 2
# %%


def get_corners_and_vertical_lines(st):
    corners = {}
    vert = defaultdict(lambda: set())
    for (x1, y1), (x2, y2), (x3, y3) in windowed(st + st[:2], 3):  # type: ignore
        dx_ab, dy_ab = x2 - x1, y2 - y1
        dx_bc, dy_bc = x3 - x2, y3 - y2

        clockwise = (dx_ab > 0 and dy_bc > 0) or (dy_ab > 0 and dx_bc < 0) or (dx_ab < 0 and dy_bc < 0) or (dy_ab < 0 and dx_bc > 0)
        corners[x2, y2] = clockwise

        if dy_ab == 0:
            vert[x2].add((min(y2, y3), max(y2, y3)))
        else:
            vert[x2].add((min(y1, y2), max(y1, y2)))

    return corners, dict(vert)


# %%
def get_horizontal_inside_ranges(y, corners, vert):
    ans = []

    # only has value when traveling on a line
    line_start = None
    for x, ranges in sorted(vert.items()):
        for y1, y2 in ranges:
            if y1 <= y <= y2:
                coord = x, y

                if coord not in corners:  # hit vertical wall, not on a corner (simple case)
                    assert not line_start, "can't hit non corner if on line"
                    ans.append(x)
                    break

                # hit a corner...

                if line_start is None:  # was not traveling on a line, but now we are
                    line_start = x
                    # we add inside segment when exiting line
                    break

                # was traveling along line, but we aren't anymore
                was_inside = len(ans) % 2 == 1

                if corners[(line_start, y)] ^ corners[coord]:  # lightning shaped path
                    if was_inside:  # inside up to this corner, now outside
                        ans.append(x)
                    else:
                        # outside up to last corner, still inside
                        ans.append(line_start)
                else:  # bump shaped path
                    if not was_inside:
                        # was only inside for the line segment
                        ans.extend([line_start, x])
                    # else: still inside nothing happens
                line_start = None
                break

    assert len(ans) % 2 == 0, f"{y}: hit uneven number of walls"

    return list(zip(ans[::2], ans[1::2]))


# %%


def is_inside(c1, c2, horizontal):
    x1, y1 = c1
    x2, y2 = c2
    min_x, max_x = min(x1, x2), max(x1, x2)

    return all(any(left <= min_x and max_x <= right for left, right in horizontal[y]) for y in range(min(y1, y2), max(y1, y2) + 1))


# %%


def part2(st):
    print("getting corners and vertical lines...")
    corners, vert = get_corners_and_vertical_lines(st)

    print("getting horizontal lines...")
    min_y, max_y = min(y for _, y in corners), max(y for _, y in corners)
    horizontal = {i: get_horizontal_inside_ranges(i, corners, vert) for i in range(min_y, max_y + 1)}

    print("checking min distance...")
    # check no vertical lines adjacent
    for h in horizontal.values():
        for h1, h2 in zip(h, h[1:]):
            assert h2[0] - h1[1] > 1

    print("calculating max area...")
    max_area = 0
    for c1, c2 in tqdm(combinations(st, 2), total=math.comb(len(st), 2)):
        if is_inside(c1, c2, horizontal):
            max_area = max(max_area, area(c1, c2))
    return max_area


# %%
part2(start)

# %%
teststart2 = [
    (2, 2),
    (4, 2),
    (4, 4),
    (6, 4),
    (6, 2),
    (8, 2),
    (8, 5),
    (10, 5),
    (10, 1),
    (12, 1),
    (12, 6),
    (7, 6),
    (7, 7),
    (9, 7),
    (9, 8),
    (4, 8),
    (4, 9),
    (2, 9),
    (2, 7),
    (5, 7),
    (5, 5),
    (3, 5),
    (3, 6),
    (1, 6),
    (1, 3),
    (2, 3),
]

# %%
part2(teststart2)
# %%
st = teststart
print("getting corners and vertical lines...")
corners, vert = get_corners_and_vertical_lines(st)
# %%
pprint(vert)

# %%

print("getting horizontal lines...")
min_y, max_y = min(y for _, y in corners), max(y for _, y in corners)
horizontal = {i: get_horizontal_inside_ranges(i, corners, vert) for i in range(min_y, max_y + 1)}

# %%
pprint(horizontal)
# %%

print("checking min distance...")
# check no vertical lines adjacent
for h in horizontal.values():
    for h1, h2 in zip(h, h[1:]):
        assert h2[0] - h1[1] > 1
# %%

print("calculating max area...")
max_area = 0
for c1, c2 in tqdm(combinations(st, 2), total=math.comb(len(st), 2)):
    if is_inside(c1, c2, horizontal):
        print(c1, c2)
        if max_area < area(c1, c2):
            print("new max area", area(c1, c2))
            max_area = area(c1, c2)
print(max_area)

# %%
is_inside((9, 8), (5, 5), horizontal)
