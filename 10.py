from util import flatten, nth
from itertools import islice


def solve(data):
    while True:
        answ = ''
        i = 0
        cutoff = 0
        while i < len(data):
            char = data[i]
            if i == len(data) - 1 or char != data[i + 1]:
                answ += str(i - cutoff + 1) + char
                cutoff = i + 1
            i += 1
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
