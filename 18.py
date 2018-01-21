from util import readinput, nth, neighbours8


def read_grid(data):
    return {(x, y): (1 if light == '#' else 0)
            for y, row in enumerate(data)
            for x, light in enumerate(row.rstrip('\n'))}


def on_off(point, grid):
    sum_neighbours = sum(
        grid[p] if p in grid else 0 for p in neighbours8(point))
    if grid[point] == 1:
        return 1 if (sum_neighbours == 2 or sum_neighbours == 3) else 0
    else:
        return 1 if sum_neighbours == 3 else 0


def solve(grid):
    while True:
        grid = {point: on_off(point, grid) for point in grid}
        yield grid


def solve2(grid, size):
    while True:
        grid[(0, 0)] = grid[(0, size - 1)] = 1
        grid[(size - 1, 0)] = grid[(size - 1, size - 1)] = 1
        grid = {point: on_off(point, grid) for point in grid}
        grid[(0, 0)] = grid[(0, size - 1)] = 1
        grid[(size - 1, 0)] = grid[(size - 1, size - 1)] = 1
        yield grid


def tests():
    grid = read_grid(readinput('18-example'))
    assert on_off((1, 0), grid) == 0
    assert on_off((2, 0), grid) == 1
    assert sum(nth(solve(grid), 4).values()) == 4
    assert sum(nth(solve2(grid, 6), 4).values()) == 17
    print('tests pass')


tests()

GRID = read_grid(readinput('18'))
print(sum(nth(solve(GRID), 99).values()))
print(sum(nth(solve2(GRID, 100), 99).values()))
