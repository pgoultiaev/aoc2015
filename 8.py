from util import readinput


def chars(data):
    return len(data.strip()) - len(eval(data.strip()))


def chars2(data):
    d = data.strip()
    return d.count('\\') + d.count('"') + 2


def tests():
    assert chars('""') == 2
    assert chars('"abc"') == 2
    assert chars('"aaa\\"aaa"') == 3
    assert chars('"\\x27"') == 5

    assert chars2('""') == 4
    assert chars2('"abc"') == 4
    assert chars2('"aaa\\"aaa"') == 6
    assert chars2('"\\x27"') == 5
    print('tests pass')


tests()

print(sum(map(chars, readinput(8))))
print(sum(map(chars2, readinput(8))))
