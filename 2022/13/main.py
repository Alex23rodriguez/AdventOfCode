import json
from itertools import zip_longest
from functools import cmp_to_key

###

test_txt = open("test.txt").read()
print(f"read {len(test_txt.splitlines())} test lines")
input_txt = open("input.txt").read()
print(f"read {len(input_txt.splitlines())} lines")

###

pcks = []
for pair in input_txt.split("\n\n"):
    a, b = pair.split()
    pcks.append((json.loads(a), json.loads(b)))

###


def cmp(a, b):
    if type(a) is type(b) is int:
        return -1 if a < b else 1 if a > b else 0

    if type(a) is type(b) is list:
        for x, y in zip_longest(a, b):
            if x is None:
                return -1
            if y is None:
                return 1
            ans = cmp(x, y)
            if ans:
                return ans
        return 0

    if type(a) is int:
        a = [a]
    else:
        b = [b]
    return cmp(a, b)


###

ans = 0
for i, (a, b) in enumerate(pcks, 1):
    ans += i if cmp(a, b) == -1 else 0
print(ans)

### PART 2

newpcks = [[[2]], [[6]]]
for a, b in pcks:
    newpcks.append(a)
    newpcks.append(b)

ordered = sorted(newpcks, key=cmp_to_key(cmp))

ind1, ind2 = 0, 0
for i, o in enumerate(ordered, 1):
    if type(o) is list and len(o) == 1 and type(o[0]) is list and len(o[0]) == 1:
        if o[0][0] == 2:
            ind1 = i
        elif o[0][0] == 6:
            ind2 = i
        if ind1 and ind2:
            break

print(ind1 * ind2)
