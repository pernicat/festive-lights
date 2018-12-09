from typing import List, Tuple
import math
import time

Pattern = List[Tuple[int]]
DELAY = 0.5
ITERATIONS = 30


def pattern_repeater(pixels, pattern: Pattern):
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

    if step > 0:
        r = range(0, len(pattern), step)
    else:
        r = range(len(pattern), 0, step)

    for _ in range(iterations):
        for l in r:
            result = pattern[l:] + pattern[0:l]
            pattern_repeater(pixels, result)
            time.sleep(delay)
