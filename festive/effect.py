"""tools for doing effects on the lights"""
from itertools import cycle

from .types import Pattern, Show


def scroll_left(pattern: Pattern) -> Show:
    while True:
        for i in range(len(pattern)):
            yield cycle(pattern[i:] + pattern[:i])


def scroll_right(pattern: Pattern) -> Show:
    while True:
        for i in range(len(pattern)):
            yield cycle(pattern[-i:] + pattern[:-i])
