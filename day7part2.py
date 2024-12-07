from dataclasses import dataclass
import itertools
import copy

@dataclass
class Row:
	result: int
	values: list[int]
	combinations: list[list]
	
	@classmethod
	def from_raw_line(cls, raw_line):
		result = int(raw_line[0])
		values = raw_line[1].rstrip("\n").split(" ")[1:]
		combinations = list(itertools.product(["*", "+", "||"], repeat=len(values)-1))
		return cls(result=result, values=values, combinations=combinations)
	
	def is_calibrated(self):
		for combination in self.combinations:
			values = copy.deepcopy(self.values)
			combination = copy.deepcopy(combination)
			combination = list(combination)
			current_value = int(values.pop(0))
			while len(values) > 0:
				operand = values.pop(0)
				current_operator = combination.pop(0)
				
				if current_operator == "*":
					current_value *= int(operand)
				if current_operator == "+":
					current_value += int(operand)
				if current_operator == "||":
					current_value = int(str(current_value) + operand) 
			if current_value == self.result:
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
