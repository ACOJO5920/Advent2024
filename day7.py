from dataclasses import dataclass
import itertools

@dataclass
class Row:
	result: int
	values: list[int]
	combinations: list[tuple]
	
	@classmethod
	def from_raw_line(cls, raw_line):
		result = int(raw_line[0])
		values = raw_line[1].rstrip("\n").split(" ")[1:]
		combinations = list(itertools.product(["*", "+"], repeat=len(values)-1))
		return cls(result=result, values=values, combinations=combinations)
	
	def is_calibrated(self):
		for combination in self.combinations:	
			total = int(self.values[0])	
			for value, operator in zip(self.values[1:], combination):
				if operator == "*":
					total *= int(value)
				if operator == "+":
					total += int(value)
			if total == self.result:
				return True
		return False


def run(filename):
	rows = []
	with open(filename) as file:	
		for line in file:
			raw_line = line.split(":")
			new_row = Row.from_raw_line(raw_line)
			rows.append(new_row)
	total = 0
	for row in rows:
		if row.is_calibrated():
			total += row.result
	return total

print(run("realtest.txt"))	
