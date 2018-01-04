from util import readinput, vector
from itertools import permutations


def distances(lines):
    dist = {}
    places = []
    for line in lines:
        d = vector(line, ' ')
        dist[(d[0], d[2])] = d[len(d) - 1]
        places.append(d[0])
        places.append(d[2])
    return dist, set(places)


def solve(dist, places):
    total_dists = list()
    for perm in permutations(places):
        total_dists.append(sum(map(lambda (x, y): dist[(x, y)] if (x, y) in dist else dist[(y, x)], zip(perm, perm[1:]))))
    return total_dists


def tests():
    d = {
        ('London', 'Dublin'): 464,
        ('London', 'Belfast'): 518,
        ('Dublin', 'Belfast'): 141
    }
    p = ['London', 'Dublin', 'Belfast']
    assert min(solve(d, p)) == 605
    print('tests pass')


tests()

dist, places = distances(readinput(9))
print(min(solve(dist, list(places))))
print(max(solve(dist, list(places))))
