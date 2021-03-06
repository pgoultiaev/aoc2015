# pylint: disable=C0103
from util import inputstr

data1 = inputstr(1)


def solve1(data):
    return data.count("(") - data.count(")")


def solve2(data):
    floor = 0
    for pos, char in enumerate(data):
        if char == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return pos + 1
    return -1


def tests():
    assert solve1(')())())') == -3
    assert solve2('()())') == 5
    assert solve2(')') == 1
    print('tests pass')


tests()

print(solve1(data1))
print(solve2(data1))
