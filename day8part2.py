from dataclasses import dataclass

@dataclass
class Antenna:
	value: str
	x: int
	y: int

@dataclass
class Antinode:
	value: str
	x: int
	y: int

def run(filename: str) -> int:
	antennas = []
	with open(filename) as file:
		x = 0
		y = 0
		for line in file:
			x = 0
			for column in line:
				if column.isalnum():
					antennas.append(Antenna(value=column, x=x, y=y))
				x += 1
			y += 1

	antinodes = []
	for antenna in antennas:
		for other_antenna in antennas:
			new_antinodes = find_antinodes_v2(antenna, other_antenna, x-2, y-1)
			if new_antinodes is not None:
				for new_antinode in new_antinodes:
					if not any((new_antinode.x, new_antinode.y) == (previous_antinode.x, previous_antinode.y) for previous_antinode in antinodes):
						antinodes.append(new_antinode)
	return len(antinodes)

def find_antinodes_of_two_antennas(antenna_1: Antenna, antenna_2: Antenna) -> tuple[Antinode, Antinode] | None:
	if antenna_1.value != antenna_2.value:
		return None
	if antenna_1 == antenna_2:
		return None
	x = antenna_2.x - antenna_1.x
	y = antenna_2.y - antenna_1.y
	antinode_1 = Antinode(value=antenna_1.value, x=antenna_1.x-x, y=antenna_1.y-y)
	antinode_2 = Antinode(value=antenna_1.value, x=antenna_2.x+x, y=antenna_2.y+y)	
	return antinode_1, antinode_2	

def find_antinodes_v2(antenna_1: Antenna, antenna_2: Antenna, x_limit: int, y_limit: int) -> list[Antinode] | None:
	if antenna_1.value != antenna_2.value:
		return None
	if antenna_1 == antenna_2:
		return None
	x = antenna_2.x - antenna_1.x
	y = antenna_2.y - antenna_1.y
	x, y = get_smallest_jump(x, y)

	initial_x = antenna_1.x
	initial_y = antenna_1.y
	new_antinodes_1 = [Antinode(value=antenna_1.value, x=initial_x-(x*multiplier), y=initial_y-(y*multiplier)) for multiplier in range(1, 40)]

	initial_x = antenna_2.x
	initial_y = antenna_2.y
	new_antinodes_2 = [Antinode(value=antenna_1.value, x=initial_x+(x*multiplier), y=initial_y+(y*multiplier)) for multiplier in range(1, 40)]
	new_antinodes_total = new_antinodes_1 + new_antinodes_2
	
	valid_antinodes = []
	for antinode in new_antinodes_total:
		if 0 <= antinode.x <= x_limit and 0 <= antinode.y <= y_limit:
			valid_antinodes.append(antinode)
	antenna_node_1 = Antinode(x=antenna_1.x, y=antenna_1.y, value=antenna_1.value)
	antenna_node_2 = Antinode(x=antenna_2.x, y=antenna_2.y, value=antenna_2.value)
	valid_antinodes += [antenna_node_1, antenna_node_2]
	return valid_antinodes

def get_smallest_jump(x_diff, y_diff):
	iteration_num = 0
	last_whole_pair = (x_diff, y_diff)
	while True:
		x_diff /= 2
		y_diff /= 2
		if not x_diff.is_integer() or not y_diff.is_integer():
			return last_whole_pair	
		last_whole_pair = (x_diff, y_diff)

print(run("realtest.txt"))
