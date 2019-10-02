"""Sometimes I doubt your commitment to sparkemotion"""
from random import random
from datetime import timedelta, datetime
from typing import Iterator, Iterable, List
from itertools import cycle

from festive.timing import show_duration
from festive.transitions import hex_timed_transition
from festive.colors import HEX, BLACK, WHITE
from festive.tools import transform_to_show

from config import Config

DEFAULT_DURATION = timedelta(seconds=1)
DEFAULT_FREQUENCY = timedelta(minutes=1)
DEFAULT_TRANSITION = timedelta(seconds=1)


class Star(Iterable[HEX]):
    """
    Star that sparkles at random times
    """
    def __init__(
            self,
            duration: timedelta = DEFAULT_DURATION,
            frequency: timedelta = DEFAULT_FREQUENCY,
            transition: timedelta = DEFAULT_TRANSITION,
            color: HEX = WHITE,
            background: HEX = BLACK
    ):
        self.duration = duration
        # we multiply by to so frequency will be the average time between sparkles
        self.frequency = frequency * 2
        self.transition = transition
        self.color = color
        self.background = background
        self._schedule = None

    def __iter__(self) -> Iterator[HEX]:
        while True:
            if datetime.now() < self.schedule:
                yield self.background
                continue

            # get brighter
            for color in hex_timed_transition(self.background, self.color, self.transition):
                yield color

            # repeats the same color for the duration of the sparkle
            for color in show_duration(cycle([self.color]), self.duration):
                yield color

            # get dimmer
            for color in hex_timed_transition(self.color, self.background, self.transition):
                yield color

            self._schedule = None

    @property
    def schedule(self) -> datetime:
        if self._schedule is None:
            self._schedule = datetime.now() + self.frequency*random()
        return self._schedule


class Sparklemotion(Iterable[List[HEX]]):

    def __init__(
            self,
            size: int = Config.LED_COUNT,
            duration: timedelta = DEFAULT_DURATION,
            frequency: timedelta = DEFAULT_FREQUENCY,
            transition: timedelta = DEFAULT_TRANSITION,
            color: HEX = WHITE,
            background: HEX = BLACK
    ):
        self.stars = []

        for _ in range(size):
            star = Star(
                duration=duration,
                frequency=frequency,
                transition=transition,
                color=color,
                background=background
            )
            self.stars.append(star)

    def __iter__(self) -> Iterator[List[HEX]]:
        for colors in transform_to_show(self.stars):
            yield colors
