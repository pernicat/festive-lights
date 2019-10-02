"""tools for doing effects on the lights"""
from datetime import timedelta
from itertools import cycle, chain
from typing import Iterable, List
from enum import Enum

from .timing import show_duration
from .tools import cycle_patterns
from .colors import HEX
from .patterns import BACKGROUND


class Direction(Enum):
    LEFT = 1
    RIGHT = -1


def scroll(pattern: List[HEX], direction: Direction = Direction.LEFT) -> Iterable[List[HEX]]:
    while True:
        for i in range(len(pattern)):
            offset = direction.value * i
            yield pattern[offset:] + pattern[:offset]


def scroll_cycle(
        pattern: List[HEX],
        duration: timedelta,
        direction: Direction = Direction.LEFT
) -> Iterable[Iterable[HEX]]:
    return show_duration(cycle_patterns(scroll(pattern, direction)), duration)


def pan(
        pattern: List[HEX],
        background: List[HEX] = None,
        direction: Direction = Direction.LEFT
) -> Iterable[List[HEX]]:
    if not pattern:
        raise Exception("pattern can not be empty")
    if not background:
        background = BACKGROUND

    steps = len(background) - len(pattern)
    is_left = direction == Direction.LEFT

    iterator = range(steps) if is_left else range(steps, 0, -1)

    for i in iterator:
        yield background[:i] + pattern + background[i + len(pattern):]


def oscillating_pan(
        pattern: List[HEX],
        background: List[HEX] = None
) -> Iterable[List[HEX]]:
    return cycle(chain(
        pan(pattern, background, Direction.LEFT),
        pan(pattern, background, Direction.RIGHT)))
