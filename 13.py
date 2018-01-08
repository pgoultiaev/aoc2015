from util import readinput, vector
from itertools import permutations


def parse(lines):
    hp = {}
    names = set()
    for line in lines:
        d = vector(line.replace('.', ''), ' ')
        happiness = d[3] if d[2] == 'gain' else -(d[3])
        hp[(d[0], d[len(d) - 1])] = happiness
        names.add(d[0])
    return hp, names


def solve(hp, names):
    total_hps = list()
    for perm in permutations(names):
        # Make list circular by adding first item as last
        perm += (perm[0], )
        total_hps.append(
            sum([hp[(x, y)] + hp[(y, x)] for (x, y) in zip(perm, perm[1:])]))
    return total_hps


def addmyself(hp, names):
    themandme = zip(names, 'I' * len(names)) + zip('I' * len(names), names)
    for item in themandme:
        hp[item] = 0
    names.add('I')
    return hp, names


def tests():
    hp = {
        ('Alice', 'Bob'): 54,
        ('Alice', 'Carol'): -79,
        ('Alice', 'David'): -2,
        ('Bob', 'Alice'): 83,
        ('Bob', 'Carol'): -7,
        ('Bob', 'David'): -63,
        ('Carol', 'Alice'): -62,
        ('Carol', 'Bob'): 60,
        ('Carol', 'David'): 55,
        ('David', 'Alice'): 46,
        ('David', 'Bob'): -7,
        ('David', 'Carol'): 41
    }
    names = ['Alice', 'Bob', 'Carol', 'David']
    assert max(solve(hp, names)) == 330
    print('tests pass')


tests()

hp_dict, n = parse(readinput(13))
print(max(solve(hp_dict, n)))
print(max(solve(*addmyself(hp_dict, n))))
