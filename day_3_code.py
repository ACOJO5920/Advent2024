import re
from dataclasses import dataclass

@dataclass
class Mul:
	position: int
	value: str
	
@dataclass
class Do:
	position: int

@dataclass
class Dont:
	position: int

def get_muls(line):
	muls = []
	for mul in re.finditer(r"mul\([0-9]{1,3},[0-9]{1,3}\)", line):
		mul_value_raw = mul.group().lstrip("mul(")[:-1].split(",")
		mul_value_int = int(mul_value_raw[0]) * int(mul_value_raw[1])
		new_mul = Mul(mul.start(), mul_value_int)	
		muls.append(new_mul)
	return muls

def get_dos(line):
	dos = []
	for do in re.finditer(r"do\(\)", line):
		new_do_position = do.start()
		dos.append(Do(new_do_position))
	return dos

def get_donts(line):
	donts = []
	for dont in re.finditer(r"don\'t\(\)", line):
		new_dont_position = dont.start()
		donts.append(Dont(new_dont_position))
	return donts

def run(filename):
	with open(filename) as file:
		objects = []
		for line in file:
			muls = get_muls(line) 
			dos = get_dos(line)
			donts = get_donts(line)
			objects.extend(muls)
			objects.extend(dos)
			objects.extend(donts)
		objects.sort(key=lambda x: x.position)
	
	negated = False
	total = 0
	for object in objects:
		print(object)
		if isinstance(object, Do):
			negated = False
		elif isinstance(object, Dont):
			negated = True
		elif isinstance(object, Mul) and not negated:
			total += object.value
	return total
					


print(run("realtest.txt"))
