#!/usr/bin/env python3
import re

# grid of 1000x1000 lamps
grid = [[False for i in range(1000)] for j in range(1000)]
pattern = re.compile(r"(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)")

cmd_fn = {
    "turn on": lambda v: True,
    "turn off": lambda v: False,
    "toggle": lambda v: not v
}


def parse(expr):
    """
    Parses an expression and returns processable data
    :param expr: the raw expression
    :return: (from, from), (to, to), cmd - to is inclusive and cmd corresponds to the strings in cmd_fn
    """
    m = pattern.search(expr)
    return (int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5))), m.group(1)


def apply_to_grid(fn, start, end):
    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            grid[x][y] = fn(grid[x][y])


def adventofcode6():
    with open("input") as file:
        for line in file:
            # parse input and apply Santa's instructions
            (start, end, cmd) = parse(line)
            apply_to_grid(cmd_fn[cmd], start, end)
        # count lamps that are on
        on = 0
        for i in range(1000):
            for j in range(1000):
                on += int(grid[i][j])
        return on

if __name__ == "__main__":
    print(adventofcode6())
