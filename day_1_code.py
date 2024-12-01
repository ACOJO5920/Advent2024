def run(file_name):
    with open(file_name) as file:
        list_1 = []
        list_2 = []
        for line in file:
            line = line.split("   ")
            line[1] = line[1].rstrip("\n")

            list_1.append(line[0])
            list_2.append(line[1])
    list_1.sort()
    list_2.sort()

    diffs = 0
    for x in range(len(list_1)):
        diffs += abs(int(list_2[x]) - int(list_1[x]))

    return diffs

def run_part_2(file_name):
    with open(file_name) as file:
        list_1 = []
        dict_2 = {}
        for line in file:
            line = line.split("   ")
            line[1] = line[1].rstrip("\n")
            list_1.append(line[0])

            if line[1] not in dict_2:
                dict_2[line[1]] = 1
            else:
                dict_2[line[1]] += 1

    diffs = 0
    for item in list_1:
        if item in dict_2:
            diffs += int(item) * dict_2[item]
    return diffs

run_part_2("realtest.txt")