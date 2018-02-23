from itertools import islice
from util import nth


def get_nth(row, column):
    y = column + (row - 1)
    z = (y * (y + 1)) // 2
    return z - (row - 1)


def gen_number(start):
    current = start
    while True:
        yield current
        current = current * 252533 % 33554393


def tests():
    assert get_nth(2, 5) == 20
    assert get_nth(3, 3) == 13
    assert get_nth(4, 1) == 7
    assert nth(gen_number(20151125), get_nth(4, 5) - 1) == 10600672
    print('tests pass')


tests()

print(nth(gen_number(20151125), get_nth(2978, 3083) - 1))
