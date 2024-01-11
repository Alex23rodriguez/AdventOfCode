from time import sleep
with open("input.txt") as f:
	input_text = f.read()
	grid = input_text.splitlines()
	m, n = len(grid), len(grid[0])

def get_adj(coord):
	i, j = coord
	tile = grid[i][j]
	
	dirs = [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]
	if tile in "^>v<":
		yield dirs["^>v<".index(tile)]
		return
	
	for d, (a, b) in enumerate(dirs):
		if a < 0 or b < 0 or a == m or b == n:
			continue
		tile = grid[a][b]
		if tile == '.':
			yield a, b
		elif (d == 0 and tile == "^") or (d == 1 and tile == ">") or (d == 2 and tile == "v") or (d == 3 and tile == "<"):
			yield a, b
			
start = 0, grid[0].index(".")
end = m - 1, grid[m - 1].index(".")
print(start, end)

def search_path():
	global best, path
	
	checkpoint = len(path)
	
	nexts = [n for n in get_adj(path[-1]) if n not in path]
	# don't recurse if no choice
	while len(nexts) == 1:
		path.append(nexts.pop())
		nexts = [n for n in get_adj(path[-1]) if n not in path]
	
	# check if at the end
	if path[-1] == end:
		steps = len(path) - 1
		print(steps)
		best = max(steps, best)
		
	# recurse options
	for nxt in nexts:
		path.append(nxt)
		search_path()
		path.pop()
	
	# go back to choice
	path = path[:checkpoint]

best = 0
path = [start]
search_path()
print('---')
print(best)
