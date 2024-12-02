def run(file_name):
    with open(file_name) as file:
        reports = []
        for line in file:
            report = line.split(" ")
            report[len(report)-1] = report[len(report)-1].rstrip("\n")
            reports.append(report)
    safe_reports = 0
    for report in reports:
        if is_safe(report):
            safe_reports += 1
            print(report)
    return safe_reports

def is_safe(report):
    previous_level = int(report[0])
    starting_level = True
    increasing = None
    for current_level in report[1:]:
        current_level = int(current_level)
        if starting_level:
            if abs(current_level - previous_level) > 3 or current_level == previous_level:
                return False
            if current_level > previous_level:
                increasing = True
                starting_level = False
            elif current_level < previous_level:
                increasing = False
                starting_level = False
            else:
                return False
        else:
            if increasing and current_level < previous_level:
                return False
            elif increasing and abs(current_level - previous_level) > 3:
                return False
            elif not increasing and current_level > previous_level:
                return False
            elif not increasing and abs(previous_level - current_level) > 3:
                return False
            elif current_level == previous_level:
                return False
        previous_level = current_level

    return True
            
def is_safe_v2(report):
    previous_level = int(report[0])
    starting_level = True
    increasing = None
    has_offence = False
    for current_level in report[1:]:
        current_level = int(current_level)
        if starting_level:
            if abs(current_level - previous_level) > 3 or current_level == previous_level:
                return False
            if current_level > previous_level:
                increasing = True
                starting_level = False
            elif current_level < previous_level:
                increasing = False
                starting_level = False
            else:
                return False
        else:
            if increasing and current_level < previous_level:
                return False
            elif increasing and abs(current_level - previous_level) > 3:
                return False
            elif not increasing and current_level > previous_level:
                return False
            elif not increasing and abs(previous_level - current_level) > 3:
                return False
            elif current_level == previous_level:
                return False
        previous_level = current_level

    return True

print(run("realtest.txt"))