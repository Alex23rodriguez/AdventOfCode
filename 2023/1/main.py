# imports
import re
import json
from itertools import (
    combinations,
    permutations,
    zip_longest,
    accumulate,
    combinations_with_replacement,
)
from collections import defaultdict, Counter
from functools import reduce, lru_cache, partial

###
test_txt = open("test.txt").read()

input_txt = open("input.txt").read()
print(f"read {len(input_txt.splitlines())} lines")
###
# read util functions


###
def prepare(inp):
    lines = inp.splitlines()
    # UPDATE
    out = []
    for l in lines:
        print(l)
        for c in l:
            if c.isdigit():
                tmp = c
                break
        for c in reversed(l):
            if c.isdigit():
                out.append(int(tmp + c))
                break

    return out


teststart = prepare(test_txt)
start = prepare(input_txt)
###
# util functions

###
# main
start
###
sum(start)
###
nums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def prepare(inp):
    lines = inp.splitlines()
    # UPDATE
    out = []

    for l in lines:
        print(l)
        tmp = ""
        for i in range(len(l)):
            c = l[i]
            if c.isdigit():
                print("caught digit start", c)
                tmp = c
                break
            else:
                for k, v in nums.items():
                    if l[i:].startswith(k):
                        tmp = v
                        break
                if tmp:
                    break

        for i in range(len(l)):
            c = l[-i - 1]
            if c.isdigit():
                print("caught digit end")
                out.append(int(tmp + c))
                break
            else:
                ext = False
                for k, v in nums.items():
                    if l[-i - 1 :].startswith(k):
                        out.append(int(tmp + v))
                        ext = True
                        break
                if ext:
                    break

        print(out[-1])

    return out


teststart = prepare(test_txt)
start = prepare(input_txt)
###
# util functions

###
# main
sum(start)
###
sum(teststart)
