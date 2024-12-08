from dataclasses import dataclass
from operator import add
import copy

@dataclass
class Player:
	x: int
	y: int
	addifier: tuple = (0, -1)

	def cycle_direction(self):
		if self.addifier == (0, -1):
			self.addifier = (1, 0)
		elif self.addifier == (1, 0):
			self.addifier = (0, 1)
		elif self.addifier == (0, 1):
			self.addifier = (-1, 0)
		elif self.addifier == (-1, 0):
			self.addifier = (0, -1)
	def move_forward(self):
		self.x = self.x + self.addifier[0]
		self.y = self.y + self.addifier[1]


@dataclass
class Obstacle:
	x: int
	y: int


def run(filename):
	with open(filename) as file:
		obstacles = []
		x_grid = []
		y = 0
		for line in file:
			x_grid.append(list(line)[:-1])
			if "^" in line:
				x = line.index("^")
				starter_player = Player(x=x, y=y)
			if "#" in line:
				for x in range(len(line)):
					if line[x] == "#":
						obstacles.append(Obstacle(x=x, y=y))	
			y+= 1		

	failed_loops = 0
	for x in range(len(x_grid)):
		for y in range(len(x_grid[0])):
			print(f"row {x} column {y} out of rows {len(x_grid)} columns {len(x_grid[0])}")
			player = copy.deepcopy(starter_player)
			reached_locations = {(player.x, player.y, player.addifier): True}
			new_obstacles = copy.deepcopy(obstacles)
			new_obstacles.append(Obstacle(x=x, y=y))
			while player.x > 0 and player.x < len(x_grid) and player.y > 0 and player.y < len(x_grid[0]):
				next_location = get_next_location(player, new_obstacles)
				if next_location in reached_locations:
					failed_loops += 1
					break
				reached_locations[next_location] = True	
	
	return failed_loops


def get_next_location(player, obstacles):
	current_location = (player.x, player.y, player.addifier)
	next_location = tuple(map(add, current_location, player.addifier)) 	
	if any(next_location == (obstacle.x, obstacle.y) for obstacle in obstacles):
		player.cycle_direction()
		current_location = (player.x, player.y, player.addifier)
		return current_location
	else:
		player.move_forward()	
	return (player.x, player.y, player.addifier)
	
print(run("realtest.txt"))
