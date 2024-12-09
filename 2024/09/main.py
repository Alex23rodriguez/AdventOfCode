# %% imports
import sys

sys.path.append("../..")
from pathlib import Path
from pprint import pprint

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
    out = [func(line) for line in lines]
    return out


# %% util defenitions


# %% parse input
def parse_line(line: str):
    # TODO
    return line


with timed():
    teststart = test_txt
    start = input_txt.replace("\n", "")

# %% main
memory = []
for i, c in enumerate(start):
    if i % 2 == 0:
        memory += [i // 2] * int(c)
    else:
        memory += [None] * int(c)
print(f"{len(memory) = }")


data_len = sum([1 for m in memory if m is not None])
print(f"{data_len = }")

while len(memory) > data_len:
    x = memory.pop()
    if x is None:
        continue
    for i, v in enumerate(memory):
        if v is None:
            memory[i] = x
            break
print("rearranged")

# memory
# %%
checksum = sum(i * v for i, v in enumerate(memory))
checksum
# %%
set(start.replace("\n", ""))
# %%
# %% PART 2
# %%
memory = {}
pos = 0
for i, c in enumerate(start):
    id = i // 2 if i % 2 == 0 else None
    memory[pos] = (id, int(c))  # id, size, pos
    pos += int(c)
# print(f'{len(memory) = }')
pprint(memory)


data_len = sum(v for id, v in memory.values() if id is not None)
print(f"{data_len = }")


def merge(memory):
    done = False
    while not done:
        done = True
        keys = list(sorted(memory.keys()))
        for k1, k2 in zip(keys, keys[1:]):
            id1, v1 = memory[k1]
            id2, v2 = memory[k2]

            if id1 is None and id2 is None:
                memory[k1] = (None, v1 + v2)
                del memory[k2]
                done = False
                break


# save for iteration in original order
init = list(reversed(memory.items()))
# print(init)

for k, (id, v) in init:
    if id is None:
        continue

    positions = sorted(memory.keys())
    for pos in positions:
        id2, v2 = memory[pos]
        if pos >= k:
            break
        if id2 is not None or v2 < v:
            continue

        # print(f"moving {id} to {pos}")
        memory[pos] = (id, v)
        memory[k] = (None, v)
        # del memory[k]
        if v < v2:
            memory[pos + v] = (None, v2 - v)
        break

    # merge
    merge(memory)

pprint(memory)

# %%
last_id = None
ans = 0
for i in range(max(memory.keys())):
    if i in memory:
        last_id = memory[i][0]
    if last_id is not None:
        ans += i * last_id
print(ans)
