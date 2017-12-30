from util import readinput, integers
from functools import partial

ops = {
    'on': (lambda x: 1),
    'off': (lambda x: 0),
    'toggle': (lambda x: 0 if x == 1 else 1)
}

ops2 = {
    'on': (lambda x: x + 1),
    'off': (lambda x: x - 1 if x > 0 else 0),
    'toggle': (lambda x: x + 2)
}


def switch_lights(data, grid, ops):
    instr, ranges = parse(data)
    for i in range(ranges[0], ranges[2] + 1):
        for j in range(ranges[1], ranges[3] + 1):
            grid[i][j] = ops[instr](grid[i][j])


def parse(data):
    d = data.split(' ')
    ranges = integers(data)
    if len(d) == 5:
        return d[1], ranges
    return 'toggle', ranges


def solve1():
    grid = [[0 for j in range(1000)] for i in range(1000)]
    switch_lights1 = partial(switch_lights, grid=grid, ops=ops)
    map(switch_lights1, readinput(6))
    print(sum(map(sum, grid)))


def solve2():
    grid = [[0 for j in range(1000)] for i in range(1000)]
    switch_lights2 = partial(switch_lights, grid=grid, ops=ops2)
    map(switch_lights2, readinput(6))
    print(sum(map(sum, grid)))


def tests():
    assert parse('turn on 0,0 through 999,999') == ('on', (0, 0, 999, 999))
    assert parse('toggle 0,0 through 999,0') == ('toggle', (0, 0, 999, 0))
    assert parse('turn off 499,499 through 500,500') == ('off', (499, 499, 500,
                                                                 500))
    assert sum(map(sum, [[0 for j in range(10)] for i in range(10)])) == 0
    print('tests pass')


tests()

solve1()
solve2()
