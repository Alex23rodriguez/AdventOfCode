### imports
# import re
# import json
# from itertools import (
#     combinations,
#     permutations,
#     zip_longest,
#     accumulate,
#     combinations_with_replacement,
# )
# from collections import defaultdict, Counter
# from functools import reduce, lru_cache, partial
#
# import sys
# sys.path.append('../..')
# import util

### read files
test_txt = open("test.txt").read()
test_lines = test_txt.splitlines()
print(f"read {len((test_lines))} test lines")
input_txt = open("input.txt").read()
input_lines = input_txt.splitlines()
print(f"read {len((input_lines))} lines")


### read functions
def parse_lines(lines: list[str]):
    out = [line_func(line) for line in lines]
    return out


###
def line_func(line: str):
    # TODO
    return line


teststart = parse_lines(test_lines)
start = parse_lines(input_lines)
###
# util functions

###
# main
