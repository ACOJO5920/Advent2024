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
			new_antinodes = find_antinodes_of_two_antennas(antenna, other_antenna)
			if new_antinodes is not None:
				if not any((antinode.x, antinode.y) == (new_antinodes[0].x, new_antinodes[0].y) for antinode in antinodes):
					antinodes.append(new_antinodes[0])
					
				if not any((antinode.x, antinode.y) == (new_antinodes[1].x, new_antinodes[1].y) for antinode in antinodes):
					antinodes.append(new_antinodes[1])
	valid_antinodes = []
	for antinode in antinodes:
		if 0 <= antinode.x <= x-2 and 0 <= antinode.y <= y-1:
			valid_antinodes.append(antinode)
	return len(valid_antinodes)

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

print(run("realtest.txt"))
