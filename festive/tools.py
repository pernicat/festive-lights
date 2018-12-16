"""functions for manipulating color patterns"""

import math
import time
from typing import Iterable
from festive.patterns import Pattern
from festive.colors import BLACK


DELAY = 0.5
ITERATIONS = 30


def pattern_repeater(pixels, pattern: Pattern):
    """repeats a pattern accross the lights"""
    multiplier = int(math.ceil(len(pixels) / len(pattern)))

    new = (pattern * multiplier)[:len(pixels)]

    for index, value in enumerate(new):
        pixels[index] = value
    pixels.show()


def scroll(pixels,
           pattern: Pattern,
           delay: float = DELAY,
           iterations: int = ITERATIONS,
           step: int = 1):
    """repeats a pattern and scrolls it across the lights"""

    if step > 0:
        shift_range = range(0, len(pattern), step)
    else:
        shift_range = range(len(pattern), 0, step)

    for _ in range(iterations):
        for shift in shift_range:
            result = pattern[shift:] + pattern[0:shift]
            pattern_repeater(pixels, result)
            time.sleep(delay)


def fill_at(pixels, position: int, pattern: Pattern = None, background=BLACK):
    """puts a pattern at a specific position"""
    if pattern:
        pixels.fill(background)
    for key, value in enumerate(pattern):
        pixels[position + key] = value


def _swipe_gen(pixels, pattern: Pattern, iterator: Iterable[int], background=BLACK, delay=0.01):
    for i in iterator:
        pixels.fill(background)
        fill_at(pixels, i, pattern, background)
        pixels.show()
        time.sleep(delay)


def swipe_right(pixels, pattern: Pattern, background=BLACK, delay=0.01):
    """moves all the pixels to the right"""
    _swipe_gen(pixels, pattern, range(len(pixels) - len(pattern)), background, delay)


def swipe_left(pixels, pattern: Pattern, background=BLACK, delay=0.01):
    """moves all the pixels to the left"""
    _swipe_gen(pixels, pattern, range(len(pixels) - len(pattern), 0, -1), background, delay)


def swipe(pixels, pattern: Pattern, background=BLACK, delay=0.01, iterations=10):
    """moves all the pixels back and forth"""
    for _ in range(iterations):
        swipe_right(pixels, pattern, background, delay)
        swipe_left(pixels, pattern, background, delay)
