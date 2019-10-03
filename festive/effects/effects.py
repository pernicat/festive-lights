"""tools for doing effects on the lights"""
import random
from datetime import timedelta
from itertools import cycle, chain
from typing import Iterable, List
from enum import Enum

from festive.timing import show_duration
from festive.tools import cycle_patterns
from festive.colors import HEX
from festive.patterns import BACKGROUND


class Direction(Enum):
    LEFT = 1
    RIGHT = -1

    @classmethod
    def random(cls):
        return random.choice(list(cls.__members__.values()))


def rotate_pattern(pattern: List[HEX], direction: Direction = Direction.LEFT) -> Iterable[List[HEX]]:
    while True:
        for i in range(len(pattern)):
            offset = direction.value * i
            yield pattern[offset:] + pattern[:offset]


def scroll(
        pattern: List[HEX],
        duration: timedelta,
        direction: Direction = Direction.LEFT
) -> Iterable[Iterable[HEX]]:
    """
    Repeats the pattern and limits the duration of a scroll
    :param pattern:
    :param duration:
    :param direction:
    :return:
    """
    return show_duration(cycle_patterns(rotate_pattern(pattern, direction)), duration)


def pan(
        pattern: List[HEX],
        background: List[HEX] = None,
        direction: Direction = Direction.LEFT
) -> Iterable[List[HEX]]:
    """
    Pan's the pattern from one side of the strip to the other
    :param pattern:
    :param background:
    :param direction:
    :return:
    """
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
    """
    Knight Ryder effect
    :param pattern:
    :param background:
    :return:
    """
    return cycle(chain(
        pan(pattern, background, Direction.LEFT),
        pan(pattern, background, Direction.RIGHT)))
