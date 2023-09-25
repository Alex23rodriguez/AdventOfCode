# imports
from itertools import permutations, combinations

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
def best_possible(opened, mins):
    global valves
    rem = 30 - mins
    s = sum(valves[o] for o in opened) * rem
    items = filter(lambda x: x[0] not in opened, valves.items())
    for _, r in items:
        if r == 0:
            break
        rem -= 2
        if rem <= 0:
            break
        s += r * rem
    return s


def get_paths(novisit):
    global valves
    keys = [k for k, v in valves.items() if k not in novisit and v > 0]
    print(keys)
    return permutations(keys)


def calc(path, rem=30, curr="AA"):
    global valves, dist
    s = 0
    for v in path:
        rem -= dist[curr][v] + 1
        if rem <= 0:
            break
        s += valves[v] * rem
        curr = v
    return s, rem

def calc_best(traversed, score, rem):
    global keys
    remkeys = set(keys) - set(traversed)
    best = 0
    bestpath = ()
    for p in permutations(remkeys):
        s = calc(p, rem, traversed[-1])[0] + score
        if s > best:
            best = s
            bestpath =traversed + p
    return best, bestpath

###
valves, tunnels = start
valves

###
graph = iden_cross(tunnels)
dist = floyd_warshall(graph)
novisit = [k for k, v in dist["AA"].items() if v == float("inf")]
keys = set([k for k, v in valves.items() if v > 0])
###
novisit
###
paths = get_paths(novisit)
###
### TOO SLOW!
best = 0
for i, path in enumerate(paths):
    r = calc(path, dist)
    if r > best:
        print(r, path)
        best = r


###
###
# all possible paths of 3
ans = {}
for p in permutations(keys, 5):
    p = tuple(reversed(p))
    ans[p] = calc(p)
###
srt = sorted(ans.values(), reverse=True)
srt[:10]
###
important = {}
for k, v in ans.items():
    if v[0] > 1800:
        print(k, v)
        important[k] = v

###
for k, (s, r) in important.items():
    print(calc_best(k, s, r))
###
###
### PART 2
###
###
ans = {}
n = 6
for i, vs in enumerate(combinations(keys, n)):
    if i % 1000 == 0:
        print(i)
    frst = vs[0]
    for p in permutations(vs):
        p1, p2 = p[:n//2], p[n//2:]
        if p2[0] == frst:
            break

        me = calc(p1, rem=26)
        ele = calc(p2, rem=26)
        ans[(p1,p2)] = me, ele
        
###
K = list(ans.keys())
###
for k in K[:10]:
    print(k, ans[k])
###
max((a[0] + b[0] for a,b in ans.values()))
###
important = {}
for k, v in ans.items():
    if v[0][0]  + v[1][0] > 1800:
        important[k] = v
###
len(important)
###
def calc_best2(traversed, scores):
    global keys
    remkeys = set(keys) - set(traversed[0]) - set(traversed[1])
    best = 0
    for p in permutations(remkeys):
        s1 = calc(p,           scores[0][1], traversed[0][-1])[0] + scores[0][0]
        s2 = calc(reversed(p), scores[1][1], traversed[1][-1])[0] + scores[1][0]
        if s1 + s2 > best:
            best = s1 + s2
    return best
###
best = 0
for i, (k, v) in enumerate(important.items()):
    print(i)
    s = calc_best2(k, v)
    if s > best:
        best = s
        print(best)

# i = 42, best = 2417 too low
###
best
###

important = {}
for k, v in ans.items():
    s = v[0][0] + v[1][0]
    if s > 1600 and s <= 1800:
        important[k] = v
len(important)
###
best = 0
besti = 0
for i, (k, v) in enumerate(important.items()):
    print(i)
    s = calc_best2(k, v)
    if s > best:
        besti = i
        best = s
        print(best)
print(besti, best)
# i = 6484, best = 2487, too low :(
