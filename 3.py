from util import inputstr

def visit(input):
    houses_visited = [(0, 0)]
    x = y = 0
    for pos, dir in enumerate(input):
        x, y = move(dir, x, y)
        houses_visited.append((x, y))

    return houses_visited

def visit2(input):
    return visit(input[::2]) + visit(input[1::2])

def move(dir, x, y):
    if   dir == '<': x -= 1
    elif dir == '>': x += 1
    elif dir == '^': y -= 1
    elif dir == 'v': y += 1
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