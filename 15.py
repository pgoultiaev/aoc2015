from util import array, readinput, flatten
from functools import reduce
from operator import mul
from itertools import permutations

factors = [list(zip(*array(readinput(15))))[i] for i in [2, 4, 6, 8, 10]]


def partition(n, k, l=0):
    '''n is the integer to partition, k is the length of partitions,
    l is the min partition element size'''
    if k < 1:
        raise StopIteration
    if k == 1:
        if n >= l:
            yield (n, )
        raise StopIteration
    for i in range(l, n + 1):
        for result in partition(n - i, k - 1, i):
            yield (i, ) + result


def score(comb, factors, cal_value=None):
    ing_properties = factors[:-1]
    scores = [
        sum(map(mul, comb, factors)) if sum(map(mul, comb, factors)) > 0 else 0
        for factors in ing_properties
    ]

    if cal_value and sum(map(mul, comb, factors[-1])) != cal_value:
        return 0
    else:
        return reduce(mul, scores)


def solve(data, factors, size, cal_value=None):
    partitions = list(partition(size, len(data), 0))
    comb_all = [[perm for perm in permutations(part, len(part))]
                for part in partitions]

    return max(
        [score(x, factors, cal_value) for x in set(list(flatten(comb_all)))])


def tests():
    comb = [44, 56]
    factors = [
        list(zip(*array(readinput('15-example'))))[i]
        for i in [2, 4, 6, 8, 10]
    ]
    assert score(comb, factors) == 62842880
    assert solve(array(readinput('15-example')), factors, 100) == 62842880
    print('tests pass')


tests()

print(solve(array(readinput(15)), factors, 100))
print(solve(array(readinput(15)), factors, 100, 500))
