from pprint import pprint

with open("input.txt") as f:
	input_str = f.read()
	grid = input_str.splitlines()
	
# util funcs
def get_adj(coord):
	i, j = coord
	for a, b in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
		if a < 0 or b < 0 or a == len(grid) or b == len(grid[0]):
			continue
		if grid[a][b] == '.':
			yield a,b

# find start
for i, row in enumerate(grid):
	if "S" in row:
		start = (i, row.index("S"))
		break


total_steps = 64
seen = {start: 0}
step = 0
while step < total_steps:
	new = set()
	for coord, s in seen.items():
		if s != step:
			continue
		for c in get_adj(coord):
			if c not in seen:
				new.add(c)
	
	step += 1
	for c in new:
		seen[c] = step

#pprint(seen)
print(len([1 for v in seen.values() if v%2 == 0]))
