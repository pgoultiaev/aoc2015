from util import inputstr


def visit(data):
    houses_visited = [(0, 0)]
    x = y = 0
    for _, direction in enumerate(data):
        x, y = move(direction, x, y)
        houses_visited.append((x, y))

    return houses_visited


def visit2(data):
    return visit(data[::2]) + visit(data[1::2])


def move(direction, x, y):
    if direction == '<':
        x -= 1
    elif direction == '>':
        x += 1
    elif direction == '^':
        y -= 1
    elif direction == 'v':
        y += 1
    return x, y


def tests():
    assert len(set(visit('>'))) == 2
    assert len(set(visit('^>v<'))) == 4
    assert len(set(visit('^v^v^v^v^v'))) == 2
    assert len(set(visit2('^v'))) == 3
    assert len(set(visit2('^>v<'))) == 3
    assert len(set(visit2('^v^v^v^v^v'))) == 11
    print('tests pass')


tests()

print(len(set(visit(inputstr(3)))))
print(len(set(visit2(inputstr(3)))))
