from util import readinput, vector


def surfacearea(line):
    l, w, h = parse(line)
    surfaces = [2 * l * w, 2 * w * h, 2 * h * l]
    return sum(surfaces) + min(surfaces) / 2


def ribbon(line):
    l, w, h = parse(line)
    sides = [l, w, h]
    sides.sort()
    return sides[0] * 2 + sides[1] * 2 + l * w * h


def parse(input):
    return vector(input, sep='x')


def tests():
    assert surfacearea('2x3x4') == 58
    assert surfacearea('1x1x10') == 43
    assert ribbon('2x3x4') == 34
    assert ribbon('1x1x10') == 14
    assert parse('2x3x4') == (2, 3, 4)
    print('tests pass')


tests()

print(sum(map(surfacearea, readinput(2))))
print(sum(map(ribbon, readinput(2))))