# %% imports
import sys

sys.path.append("../..")
from pathlib import Path

from more_itertools import sliced

# %% read files
test_txt = Path("test.txt").read_text().replace("\n", "")
input_txt = Path("input.txt").read_text()


# %% read functions
def get_start(txt):
    return [(int(a), int(b)) for a, b in [t.split("-") for t in txt.split(",")]]


teststart = get_start(test_txt)
start = get_start(input_txt)


# %% main
def part1(st):
    invalid = []
    for a, b in st:
        for i in range(a, b + 1):
            t = str(i)
            length = len(t)
            if length % 2 == 1:
                continue
            if t[: length // 2] == t[length // 2 :]:
                invalid.append(i)

    print(sum(invalid))


part1(start)

# %%
print(start)


# %%
# %% PART 2
# %%
def part2(st):
    invalid = set()
    for a, b in st:
        # print(a, "-", b)
        for i in range(a, b + 1):
            t = str(i)
            length = len(t)

            for repeats in range(2, length + 1):
                if length % repeats != 0:
                    continue
                # print(i, "repeats", repeats)

                slices = list(sliced(t, length // repeats, strict=True))
                # print(slices)
                if all(s == slices[0] for s in slices[1:]):
                    # print(i)
                    invalid.add(i)

    print(sum(invalid))


part2(start)
