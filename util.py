"""Utility functions for input and parsing (taken from Peter Norvig)
"""
import re
from itertools import chain, islice


def readinput(day):
    "Open this day's input file."
    return open('data/{}.txt'.format(day))


def inputstr(day):
    "The contents of this day's input file as a str."
    return readinput(day).read().rstrip('\n')


def array(lines):
    """Parse an iterable of str lines into a 2-D array.
    If `lines` is a str, splitlines."""
    if isinstance(lines, str):
        lines = lines.splitlines()
    return mapt(vector, lines)


def vector(line, sep=','):
    "Parse a str into a tuple of atoms (numbers or str tokens)."
    return mapt(atom, line.replace(sep, ' ').split())


def integers(text):
    "Return a tuple of all integers in a string."
    return mapt(int, re.findall(r'-?\b\d+\b', text))


def atom(token):
    "Parse a str token into a number, or leave it as a str."
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token


def mapt(func, *args):
    "Do a map, and make the results into a tuple."
    return tuple(map(func, *args))


# Functions on Iterables
def subsequences(seq, n):
    return [seq[i:i + n] for i in range(len(seq) + 1 - n)]


def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)


def nth(iterable, n, default=None):
    "Returns the nth item of iterable, or a default value"
    return next(islice(iterable, n, None), default)
