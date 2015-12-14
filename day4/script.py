from hashlib import md5 as h


def adventofcode4(startswith="00000", _input="iwrupvqb"):
    number = -1
    myhash = ""
    while not myhash.startswith(startswith):
        number += 1
        hashthis = _input + str(number)
        myhash = h(hashthis.encode("utf-8")).hexdigest()
    return number, myhash

data = "iwrupvqb"
fivezeros = adventofcode4("00000", data)
print("The secret number is {0}. md5({1}{0}) = {2}".format(fivezeros[0], data, fivezeros[1]))
sixzeros = adventofcode4("000000", data)
print("The secret number is {0}. md5({1}{0}) = {2}".format(sixzeros[0], data, sixzeros[1]))
