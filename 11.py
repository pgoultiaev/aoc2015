from util import subsequences

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_STRAIGHTS3 = list(zip(ALPHABET, ALPHABET[1:], ALPHABET[2:]))


def increment(data, index=1):
    i = ALPHABET.index(data[len(data) - index])

    suffix = ''
    if index > 1:
        suffix = data[len(data) - index + 1:]
    data = data[:-index] + ALPHABET[(i + 1) % len(ALPHABET)] + suffix

    if data[len(data) - index] == 'a':
        data = increment(data, index + 1)
    return data


def valid(data):
    forbidden = ['i', 'o', 'l']
    if any([f in data for f in forbidden]):
        return False

    filtered_pairs = list(filter(lambda x: x[0] == x[1], subsequences(data, 2)))
    if not any([a != b for a, b in zip(filtered_pairs, filtered_pairs[1:])]):
        return False

    data_straights3 = list(zip(data, data[1:], data[2:]))
    if not any([x == y for x in ALPHABET_STRAIGHTS3 for y in data_straights3]):
        return False
    return True


def solve(pw):
    while True:
        pw = increment(pw)
        if valid(pw):
            return pw


def tests():
    assert 'abcdefghijklmnopqrstuvwxyz'.index('b') == 1
    assert increment('xx') == 'xy'
    assert increment('xy') == 'xz'
    assert increment('xz') == 'ya'
    assert increment('ya') == 'yb'
    assert not valid('hijklmmn')
    assert not valid('abbceffg')
    assert valid('abcdffaa')
    assert valid('ghjaabcc')
    assert solve('abcdefgh') == 'abcdffaa'
    print('tests pass')


tests()

part1 = solve('vzbxkghb')
print(part1)
print(solve(part1))
