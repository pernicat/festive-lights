"""tools for doing effects on the lights"""
from itertools import cycle
from typing import Iterable, List

from .colors import HEX


def scroll_left(pattern: List[HEX]) -> Iterable[Iterable[HEX]]:
    while True:
        for i in range(len(pattern)):
            yield cycle(pattern[i:] + pattern[:i])


def scroll_right(pattern: List[HEX]) -> Iterable[Iterable[HEX]]:
    while True:
        for i in range(len(pattern)):
            yield cycle(pattern[-i:] + pattern[:-i])
