from util import integers, inputstr
from json import loads


def solve(json):
    if type(json) is int:
        return json
    elif type(json) is list:
        return sum([solve(j) for j in json])
    if type(json) != dict or 'red' in json.values():
        return 0
    return solve(list(json.values()))


def tests():
    assert solve(loads('[1,{"c":"red", "d":{"c":"red", "f": {"a": 22} },"b":2},3]')) == 4
    print('tests pass')


tests()

print(sum(integers(inputstr(12))))
print(solve(loads(inputstr(12))))
