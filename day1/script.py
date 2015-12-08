floor = 0
pos = 0
count = 0
with open("input") as file:
    for line in file:
        for c in line:
            count += 1
            if c == "(":
                floor += 1
            elif c == ")":
                floor -= 1
            if pos == 0 and floor == -1:
                pos = count
    print("Floor after completion: {}".format(floor))
    print("Position of first character causing floor -1: {}".format(pos))