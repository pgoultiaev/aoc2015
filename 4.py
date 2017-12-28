import hashlib


def solve(data, leading_zeroes):
    for i in range(10**10):
        hash_hex = hashlib.md5(bytes(data + str(i), 'utf-8')).hexdigest()
        if hash_hex[:leading_zeroes] == '0' * leading_zeroes:
            return i
    return -1


def tests():
    assert solve('abcdef', 5) == 609043
    assert solve('pqrstuv', 5) == 1048970
    print('tests pass')


tests()

print(solve('iwrupvqb', 5))
print(solve('iwrupvqb', 6))
