from util import flatten, nth
from itertools import islice


def solve(data):
    while True:
        answ = ''
        cutoff = 0
        for pos, char in enumerate(data):
            if pos == len(data) - 1 or char != data[pos + 1]:
                answ += str(pos - cutoff + 1) + str(char)
                cutoff = pos + 1
        data = answ
        yield data


def tests():
    assert list(islice(solve('1'),
                       5)) == ['11', '21', '1211', '111221', '312211']
    assert len(nth(solve('1'), 4)) == 6
    print('tests pass')


tests()

print(len(nth(solve('1321131112'), 40 - 1)))
print(len(nth(solve('1321131112'), 50 - 1)))
