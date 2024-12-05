def run(filename):
	with open(filename) as file:
		x_grid = []
		for line in file:
			x_grid.append(list(line[:-1]))	
	x = 0
	y = 0
	total = 0
	for row in x_grid:
		for col in row:
			position_xmas_num = get_positions(x, y, x_grid)
			if position_xmas_num:
				total += 1
			x += 1
		x = 0
		y += 1	
	print(total)
	return total	

def get_positions(x, y, grid):
	possible_directions = []
	x_limit = len(grid)-1
	y_limit = len(grid[0])-1
	for direction in [return_left_diag_coords, return_right_diag_coords]:
		if any(coords_set[1] < 0 for coords_set in direction(x, y)):
			pass
		
		elif any(coords_set[0] < 0 for coords_set in direction(x, y)):
			pass

		elif any(coords_set[0] > x_limit for coords_set in direction(x, y)):
			pass

		elif any(coords_set[1] > y_limit for coords_set in direction(x, y)):
			pass
		else:
			possible_directions.append(direction)
	total = 0
	for direction in possible_directions:
		discovered_values = [grid[y][x] for x, y in direction(x, y)]
		if "".join(discovered_values) == "MAS" or "".join(discovered_values) == "SAM":
			total += 1
	return total == 2

def return_left_diag_coords(x, y):
	return [(x-1, y-1), (x, y), (x+1, y+1)]
def return_right_diag_coords(x, y):
	return [(x-1, y+1), (x, y), (x+1, y-1)]

run("realtest.txt")
