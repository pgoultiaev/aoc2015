from itertools import combinations
from util import array, readinput

HEALTH = 100
WEAPONS = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
ARMOR = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
RINGS = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0,
                                                                       3)]

GEAR = [
    tuple(map(sum, zip(w, a, *rings)))
    for w in WEAPONS for a in ARMOR for c in range(3)
    for rings in combinations(RINGS, c)
]


def fight(boss, player_health, gear):
    boss_health = boss[0]
    while player_health > 0:
        boss_health -= gear[1] - boss[2] if gear[1] - boss[2] > 1 else 1
        if boss_health <= 0:
            return 1
        player_health -= boss[1] - gear[2] if boss[1] - gear[2] > 1 else 1
    return -1


def solve(boss, player_health):
    return min(
        [g for g in GEAR if fight(boss, player_health, g) == 1],
        key=lambda g: g[0])


def solve2(boss, player_health):
    return max(
        [g for g in GEAR if fight(boss, player_health, g) == -1],
        key=lambda g: g[0])


def tests():
    boss = (12, 7, 2)
    assert fight(boss, 8, ('x', 5, 5)) == 1
    print('tests pass')


tests()

BOSS = tuple([x[-1] for x in array(readinput(21))])
print(solve(BOSS, 100))
print(solve2(BOSS, 100))