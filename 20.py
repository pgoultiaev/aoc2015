from itertools import islice
from math import sqrt


def solve(data):
    for house in range(1, int(data / 10) + 1):
        if sum([
                e + house / e for e in range(1, int(sqrt(house) + 1))
                if house % e == 0
        ]) * 10 >= data:
            return house


def solve2(data):
    for house in range(1, int(data / 11) + 1):
        divs = list()
        for e in range(1, int(sqrt(house) + 1)):
            if house % e == 0:
                if e * 50 >= house:
                    divs.append(e)
                if int(house / e) * 50 >= house:
                    divs.append(int(house / e))
        if sum(divs) * 11 >= data:
            return house


def tests():
    assert solve(140) == 8
    assert solve(70) == 4
    print('tests pass')


tests()

print(solve2(29000000))
