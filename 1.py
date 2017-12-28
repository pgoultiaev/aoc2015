from util import *

data1 = inputstr(1)

def solve1(input):
    return input.count("(") - input.count(")")

def solve2(input):
    floor = 0
    for pos, char in enumerate(input):
        if char == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return pos + 1

def tests():
    assert solve1(')())())') == -3
    assert solve2('()())') == 5
    assert solve2(')') == 1
    print('tests pass')

tests()

print(solve1(data1))
print(solve2(data1))
