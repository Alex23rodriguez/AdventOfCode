filename = '13.txt'

with open(filename) as f:
  input = f.read().split('\n\n')

###
import json

pcks = []
for pair in input:
  a,b = pair.split()
  pcks.append((json.loads(a), json.loads(b)))

###
from itertools import zip_longest

def cmp(a,b):
  if type(a) is type(b) is int:
    return -1 if a < b else 1 if a>b else 0
  
  if type(a) is type(b) is list:
    for x,y in zip_longest(a,b):
      if x is None:
        return -1
      if y is None:
        return 1
      ans = cmp(x,y)
      if ans:
        return ans
    return 0

  if type(a) is int:
    a = [a]
  else:
    b = [b]
  return cmp(a,b)

###

ans = 0
for i, (a,b) in enumerate(pcks, 1):
  ans += i if cmp(a,b)==-1 else 0
print(ans)

### PART 2
from functools import cmp_to_key

newpcks = [ [[2]], [[6]] ]
for a,b in pcks:
  newpcks.append(a)
  newpcks.append(b)

ordered = sorted(newpcks, key=cmp_to_key(cmp))

ind1, ind2 = 0,0
for i, o in enumerate(ordered,1):
  if type(o) is list and len(o) == 1 and type(o[0]) is list and len(o[0]) == 1:
    if o[0][0] == 2:
      ind1 = i
    elif o[0][0] == 6:
      ind2 = i
    if ind1 and ind2:
      break

print(ind1*ind2)
