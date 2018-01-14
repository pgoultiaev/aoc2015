from util import integers, readinput, array


def fly(speed, dur, rest, time):
    main = int(time / (dur + rest)) * (speed * dur)
    rest = time % (dur + rest) if time % (dur + rest) <= dur else dur
    return main + (rest * speed)


def solve2(data, total):
    points = [0] * len(data)

    for t in range(1, total):
        dist = [fly(inp[3], inp[6], inp[13], t) for inp in data]
        points = [
            x + 1 if dist[pos] == max(dist) else x
            for pos, x in enumerate(points)
        ]
    return max(points)


def tests():
    assert fly(14, 10, 127, 1000) == 1120
    assert fly(16, 11, 162, 1000) == 1056
    assert solve2(array(readinput('14-example')), 1000) == 689
    print('tests pass')


tests()

print(
    max([
        fly(inp[0], inp[1], inp[2], 2503)
        for inp in map(integers, readinput(14))
    ]))

print(solve2(array(readinput(14)), 2503))
