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
				total += position_xmas_num						
			x += 1
		x = 0
		y += 1	
	print(total)
	return total	

def get_positions(x, y, grid):
	possible_directions = []
	x_limit = len(grid)-1
	y_limit = len(grid[0])-1
	for direction in [return_north_coords, return_north_west_coords, return_north_east_coords, return_east_coords, return_south_coords, return_south_west_coords, return_south_east_coords, return_west_coords]:
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
		if "".join(discovered_values) == "XMAS": 
			total += 1
	return total

def return_north_coords(x, y):
	return [(x, y), (x, y-1), (x, y-2), (x, y-3)]
def return_north_west_coords(x, y):
	return [(x, y), (x-1, y-1), (x-2, y-2), (x-3, y-3)]
def return_north_east_coords(x, y):
	return [(x, y), (x+1, y-1), (x+2, y-2), (x+3, y-3)]
def return_east_coords(x, y):
	return [(x, y), (x+1, y), (x+2, y), (x+3, y)]
def return_south_coords(x, y):
	return [(x, y), (x, y+1), (x, y+2), (x, y+3)]
def return_south_west_coords(x, y):
	return [(x, y), (x-1, y+1), (x-2, y+2), (x-3, y+3)]
def return_south_east_coords(x, y):
	return [(x, y), (x+1, y+1), (x+2, y+2), (x+3, y+3)]
def return_west_coords(x, y):
	return [(x, y), (x-1, y), (x-2, y), (x-3, y)]

run("realtest.txt")
