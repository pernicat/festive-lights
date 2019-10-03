from datetime import timedelta
from itertools import product
from typing import Iterable, Iterator, List, Tuple
from random import choice, uniform

from festive.effects import Direction, scroll
from festive.colors import HEX, BLACK
from festive.patterns import color_combos, adjustment
from festive.timing import limit

ADJUSTMENT_RANGE = 6


class Theme(Iterable):

    def __init__(self, colors: List[HEX], duration: timedelta, background: HEX = BLACK):
        self.duration = duration
        self.background = background
        self.colors = colors

        self._color_combos = None
        self._adjustment_options = None
        self._patterns = None

    def __iter__(self) -> Iterator[Iterable[HEX]]:
        while True:
            pattern = choice(self.patterns)
            refresh = timedelta(seconds=uniform(0.1, 0.7))

            for colors in limit(scroll(pattern, self.duration, Direction.random()), refresh):
                yield colors

    @property
    def patterns(self) -> List[List[HEX]]:
        if not self._patterns:
            self._patterns = [adjustment(*args) for args in self.adjustment_args]

        return self._patterns

    @property
    def background_options(self) -> List[HEX]:
        return [self.background] + self.colors

    @property
    def adjustment_args(self) -> List[Tuple[List[HEX], int, int, HEX]]:
        if not self._adjustment_options:
            args_product = product(
                self.color_combos,
                range(1, ADJUSTMENT_RANGE),
                range(ADJUSTMENT_RANGE),
                self.background_options)

            def filter_(colors: List[HEX], width: int, padding: int, background: HEX) -> bool:
                if width < 1:
                    raise Exception("width must be at least one")
                if background in colors:
                    return False

                if len(colors) == 1 and padding == 0:
                    return False

                return True

            # filters items where the background matches one of the colors
            self._adjustment_options = [args for args in args_product if filter_(*args)]

        return self._adjustment_options

    @property
    def color_combos(self) -> List[List[HEX]]:
        if not self._color_combos:
            self._color_combos = color_combos(self.colors)

        return self._color_combos
