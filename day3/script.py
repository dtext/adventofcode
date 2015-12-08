houses = set()
x, y = 0, 0
rx, ry = 0, 0
houses = set()
houses.add((0, 0))

def parse(c, tx, ty):
    if c == ">":
        tx += 1
    elif c == "<":
        tx -= 1
    elif c == "^":
        ty += 1
    elif c == "v":
        ty -= 1
    houses.add((tx, ty))
    return tx, ty

with open("input") as file:
    for line in file:
        i = 0
        rem = ""
        if len(line) % 2:
            rem = line[-1]
            line = line[:-1]
        while i < len(line):
            santa_c, robo_c = line[i], line[i+1]
            i += 2
            x, y = parse(santa_c, x, y)
            rx, ry = parse(robo_c, rx, ry)
        if rem != "":
            x, y = parse(rem, x, y)
    print("{} houses received at least 1 present.".format(len(houses)))
