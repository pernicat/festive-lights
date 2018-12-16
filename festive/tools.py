"""functions for manipulating color patterns"""

from typing import List, Tuple
import math
import time

Pattern = List[Tuple[int]]
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
