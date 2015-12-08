import re

patterns = [
    # at least 3 vowels
    re.compile(r".*[aeiou].*[aeiou].*[aeiou].*"),
    # at least one double character
    re.compile(r".*(\w)\1.*"),
    # does not contain ab, cd, pq, xy
    re.compile(r"^((?!(?:ab|cd|pq|xy)).)*$")
]


def matchesrules(string):
    for p in patterns:
        if p.match(string) is None:
            return False
    return True


def adventofcode5():
    counter = 0
    with open("input") as file:
        for string in file:
            if matchesrules(string):
                counter += 1
    print("Number of nice words: {}".format(counter))

if __name__ == "__main__":
    adventofcode5()