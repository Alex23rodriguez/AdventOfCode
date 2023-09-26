# imports
from itertools import permutations, combinations
from datetime import datetime

###
import sys

sys.path.append("../..")
from util import floyd_warshall, iden_cross


###
test_txt = open("test.txt").read()

input_txt = open("input.txt").read()
print(f"read {len(input_txt.splitlines())} lines")
###
# read util functions


###
def prepare(inp):
    lines = inp.splitlines()
    valves = {}
    tunnels = {}
    for l in lines:
        a, b = l.split("; ")
        v = a.split()[1]
        valves[v] = int(a.split("=")[-1])
        t = b.split(" ", 4)[-1].split(", ")
        tunnels[v] = t

    valves = dict(sorted(valves.items(), key=lambda x: x[1], reverse=True))
    return valves, tunnels


def check_test():
    global test
    testans = None  # UPDATE
    assert test == testans, "test should be {testans}, but instead was {test}"


teststart = prepare(test_txt)
start = prepare(input_txt)


###
# util functions
def search(left: set, curr: str, rem: int, dist, valves):
    # print(f"just got to {curr} with {rem} minutes remaining")
    if len(left) == 0:
        # print("nowhere left to go")
        return 0
    best = 0
    for k in left:
        d = dist[curr][k] + 1
        if rem <= d:
            # print(f"cant visit {k}")
            # not enough time to visit and turn on
            continue
        # add score visiting would give
        score = valves[k] * (rem - d)
        # print(f"visiting {k} will yield {score}")
        score += search(left - set([k]), k, rem - d, dist, valves)
        if score > best:
            # print(f"its best to go {curr} -> {k}")
            best = score
    return best


###
valves, tunnels = start
valves
###
graph = iden_cross(tunnels)
dist = floyd_warshall(graph)
keys = set([k for k, v in valves.items() if v > 0])
###
print(datetime.now())
ans = search(keys, "AA", 30, dist, valves)
print("done!", ans)
print(datetime.now())
