
def run(filename):
	rule_values = []
	update_values = []
	successful_updates = []
	total = 0
	with open(filename) as file:
		for line in file:
			if "|" in line:
				rule_values.append(format_rule(line))
			elif "," in line:
				update_values.append(format_update(line))	
		for update in update_values:
			if is_valid_update(update, rule_values):
				successful_updates.append(update)
	for update in successful_updates:
		midpoint = len(update)//2	
		total += update[midpoint]
	return total

def is_valid_update(update, rule_values):
	previous_numbers = []
	future_bad_numbers = []
	for page_num in update:
		if page_num in future_bad_numbers:
			return False
		if is_being_past_infringed(page_num, rule_values, previous_numbers):
			return False
		previous_numbers.append(page_num)
		future_bad_numbers.extend(get_future_bad_numbers(page_num, rule_values))	
	return True		
			
def is_being_past_infringed(number, rule_values, previous_numbers):
	for value_set in rule_values:
		if value_set[0] == number and value_set[1] in previous_numbers:
			return True
	return False
	

def get_future_bad_numbers(number, rule_values):
	bad_numbers = []
	for value_set in rule_values:
		if value_set[1] == number:
			bad_numbers.append(value_set[0])	
	return bad_numbers

def format_rule(line):
	cleaned_line = line.rstrip("\n")
	values = cleaned_line.split("|")
	return [int(value) for value in values]

def format_update(line):
	cleaned_line = line.rstrip("\n")
	values = cleaned_line.split(",")
	return [int(value) for value in values]

print(run("realtest.txt"))
