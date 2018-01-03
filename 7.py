from util import readinput
from functools import partial
import re


def resolve(wire, wires, ops):
    if isinstance(wire, int):
        return wire
    if not isinstance(wires[wire], tuple):
        return wires[wire]

    op, args = wires[wire]
    resolved = [resolve(w, wires, ops) for w in args]
    res = ops[op](*resolved)
    wires[wire] = res
    return res


def run(data, wires):
    op = re.sub('[^A-Z]', '', data)
    args = re.compile("[a-z0-9]+").findall(data)
    args_values = [int(x) if x.isdigit() else x for x in args]
    target_wire = args_values.pop()

    if not op:
        op = 'ASSIGN'
    wires[target_wire] = (op, tuple(args_values))


def solve1(filename, wire, override_val=None):
    wires = {}
    ops = {
        'ASSIGN': lambda a: a,
        'AND': lambda a, b: a & b,
        'OR': lambda a, b: a | b,
        'LSHIFT': lambda a, b: a << b,
        'RSHIFT': lambda a, b: a >> b,
        'NOT': lambda a: (1 << 16) - 1 - a,
    }

    run1 = partial(run, wires=wires)
    map(run1, readinput(filename))

    if override_val:
        wires['b'] = override_val
    return resolve(wire, wires, ops)


def solve2():
    a_val = solve1(7, 'a')
    return solve1(7, 'a', a_val)


def tests():
    assert solve1('7-example', 'i') == 65079
    print('tests pass')


tests()

print(solve1(7, 'a'))
print(solve2())
