# imports

###
YEAR = 2022
DAY = 0

filename = f"{YEAR}/{DAY}.txt"
txt = open(filename).read()
lines = txt.splitlines()
print(f"read {len(lines)} lines")
###

for line in txt.splitlines():
    pass
