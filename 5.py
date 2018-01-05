from util import readinput, subsequences


def valid(data):
    vowels = "aeiou"
    forbidden = ['ab', 'cd', 'pq', 'xy']

    enough_vowels = len([char for char in data if char in vowels]) >= 3
    no_forbiddenwords = not any([f in data for f in forbidden])
    has_consec_chars = any([a == b for a, b in zip(data, data[1:])])

    if enough_vowels and no_forbiddenwords and has_consec_chars:
        return 1
    return 0


def valid2(data):
    pairs = subsequences(data, 2)
    has_repeating_pairs = any(
        [pairs[i + 2:].count(pair) > 0 for i, pair in enumerate(pairs)])

    has_letter_repeat = any([a == b for a, b in zip(data, data[2:])])

    if has_repeating_pairs and has_letter_repeat:
        return 1
    return 0


def tests():
    assert valid('ugknbfddgicrmopn') == 1
    assert valid('aaa') == 1
    assert valid('jchzalrnumimnmhp') == 0
    assert valid('haegwjzuvuyypxyu') == 0
    assert valid('dvszwmarrgswjxmb') == 0

    # Part two
    assert valid2('qjhvhtzxzqqjkmpb') == 1
    assert valid2('xxyxx') == 1
    assert valid2('uurcxstgmygtbstg') == 0
    assert valid2('ieodomkazucvgmuy') == 0
    print('tests pass')


tests()

print(sum(map(valid, readinput(5))))
print(sum(map(valid2, readinput(5))))
