#!/usr/bin/env python3

import re
pattern = "(\d+)x(\d+)x(\d+)"

paper = 0
ribbon = 0

with open("input") as file:
    for line in file:
        m = re.search(pattern, line)
        l, w, h = int(m.group(1)), int(m.group(2)), int(m.group(3))
        # calculate paper area
        a, b, c = l*w, w*h, h*l
        paper += 2*a + 2*b + 2*c + min(a, b, c)
        # calculate ribbon length
        dims = [l, w, h]
        smallest = min(dims)
        dims.remove(smallest)
        second = min(dims)
        ribbon += 2 * smallest + 2 * second + l * w * h
    print("Total amount of wrapping paper: {}".format(paper))
    print("Total amount of ribbon:         {}".format(ribbon))

