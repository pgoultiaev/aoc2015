from itertools import combinations
from util import flatten, array, readinput


def solve(data, total):
    all_combs = [list(combinations(data, r)) for r in range(len(data))]
    return len([c for c in list(flatten(all_combs)) if sum(c) == total])


def solve2(data, total):
    all_combs = [list(combinations(data, r)) for r in range(len(data))]
    return len(list(filter(lambda x: len(x) > 0,
                           [[c for c in c_r if sum(c) == total]
                            for c_r in all_combs]))[0])


def tests():
    assert solve([20, 15, 10, 5, 5], 25) == 4
    assert solve2([20, 15, 10, 5, 5], 25) == 3
    print('tests pass')


tests()

STORAGE = [line[0] for line in array(readinput(17))]
print(solve(STORAGE, 150))
print(solve2(STORAGE, 150))
