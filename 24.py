from util import array, readinput
from itertools import combinations
from operator import mul
from functools import reduce

PACKAGES = [int(line) for line in readinput(24)]


def solve(packages, target):
    for i in range(1, len(packages)):
        combs = [c for c in combinations(packages, i) if sum(c) == target]
        if combs:
            return reduce(mul, combs[0])


def tests():
    p = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
    assert solve(p, sum(p) / 3) == 99
    print('tests pass')


tests()

print(solve(PACKAGES, sum(PACKAGES) / 3))
print(solve(PACKAGES, sum(PACKAGES) / 4))
