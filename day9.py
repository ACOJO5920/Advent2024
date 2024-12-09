def run(filename):
	with open(filename) as file:
		for line in file:
			input_string = line.rstrip("\n")

	memory_chain = []
	ix = 0
	block_num = 0
	for value in input_string:
		if ix % 2 == 0:
			new_value = int(value)*[str(block_num)]
			memory_chain.extend(list(new_value))
			block_num += 1
		else:
			memory_chain.extend(list(int(value)*"."))
		ix += 1
	iy = len(memory_chain) - 1
	while not memory_chain[iy].isnumeric():
		iy -= 1
	for ix in range(len(memory_chain)):
		if ix >= iy:
			break
		if not memory_chain[ix].isnumeric():
			memory_chain[ix] = memory_chain[iy]
			memory_chain[iy] = "."
			iy -= 1
			while not memory_chain[iy].isnumeric():
				iy -= 1
	
	print(memory_chain)
	total = 0
	ix = 0
	for value in memory_chain:
		if value.isnumeric():
			total += int(value) * ix
		ix += 1
	print(total)
run("realtest.txt")	
