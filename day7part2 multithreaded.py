from dataclasses import dataclass
from concurrent.futures import ProcessPoolExecutor
import itertools
import copy
import time

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
				return self.result
		return 0

def divide_chunks(full_list, chunk_size):
	for x in range(0, len(full_list), chunk_size):
		yield full_list[x:x+chunk_size]

def process_chunk(rows):
	total = 0
	for row in rows:
		if row.is_calibrated():
			total += row.result
	return total	

def run(filename):
	rows = []
	with open(filename) as file:	
		for line in file:
			raw_line = line.split(":")
			new_row = Row.from_raw_line(raw_line)
			rows.append(new_row)
	total = 0
	chunks = list(divide_chunks(rows, 10))	
	start_time = time.time()	
	with ProcessPoolExecutor() as executor:
		futures = [executor.submit(process_chunk, chunk) for chunk in chunks]
	for future in futures:
		if future.result():
			total += future.result()
	print(f"end {time.time() - start_time}")
	return total

if __name__ == "__main__":	
	print(run("realtest.txt"))	
