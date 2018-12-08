from typing import List, Tuple
import math


def pattern_repeater(pixels, pattern: List[Tuple[int]]):
    multiplier = int(math.ceil(len(pixels) / len(pattern)))

    new = (pattern * multiplier)[:len(pixels)]

    for index, value in enumerate(new):
        pixels[index] = value
