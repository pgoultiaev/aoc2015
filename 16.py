from util import readinput, vector, subsequences

TAPE_DATA = [('children', 3), ('cats', 7), ('samoyeds', 2), ('pomeranians', 3),
             ('akitas', 0), ('vizslas', 0), ('goldfish', 5), ('trees', 3),
             ('cars', 2), ('perfumes', 1)]


def valid():
    for line in readinput(16):
        sue = vector(line.replace(':', '').replace(',', ''))
        sue_props = subsequences(sue, 2)[::2]
        if all([prop in TAPE_DATA for prop in sue_props[1:]]):
            yield sue_props[0][1]


def validEncabulator():
    for line in readinput(16):
        sue = vector(line.replace(':', '').replace(',', ''))
        sue_props = subsequences(sue, 2)[::2]
        for key, val in sue_props[1:]:
            if key == 'cats':
                if not val > TAPE_DATA[1][1]:
                    break
            elif key == 'trees':
                if not val > TAPE_DATA[7][1]:
                    break
            elif key == 'pomeranians':
                if not val < TAPE_DATA[3][1]:
                    break
            elif key == 'goldfish':
                if not val < TAPE_DATA[6][1]:
                    break
            elif (key, val) not in TAPE_DATA:
                break
            sue_props.remove((key, val))
        if len(sue_props) == 1:
            yield sue_props[0][1]


print(next(valid()))
print(next(validEncabulator()))
