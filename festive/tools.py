"""functions for manipulating color patterns"""
import math
import time
import random
from typing import Iterable, Iterator, Generator, Callable, List

from .colors import HEX, BLACK, WHITE


ColorGenerator = Generator[HEX, None, None]

DELAY = 0.5
ITERATIONS = 30


def pattern_repeater(pixels, pattern: List[HEX]):
    """repeats a pattern accross the lights"""
    multiplier = int(math.ceil(len(pixels) / len(pattern)))

    new = (pattern * multiplier)[:len(pixels)]

    for index, value in enumerate(new):
        pixels[index] = value
    pixels.show()


def scroll(pixels,
           pattern: List[HEX],
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


def fill_at(pixels, position: int, pattern: List[HEX] = None, background=BLACK):
    """puts a pattern at a specific position"""
    if pattern:
        pixels.fill(background)
    for key, value in enumerate(pattern):
        pixels[position + key] = value


def _swipe_gen(pixels, pattern: List[HEX], iterator: Iterable[int], background=BLACK, delay=0.01):
    for i in iterator:
        pixels.fill(background)
        fill_at(pixels, i, pattern, background)
        pixels.show()
        time.sleep(delay)


def swipe_right(pixels, pattern: List[HEX], background=BLACK, delay=0.01):
    """moves all the pixels to the right"""
    _swipe_gen(pixels, pattern, range(len(pixels) - len(pattern)), background, delay)


def swipe_left(pixels, pattern: List[HEX], background=BLACK, delay=0.01):
    """moves all the pixels to the left"""
    _swipe_gen(pixels, pattern, range(len(pixels) - len(pattern), 0, -1), background, delay)


def swipe(pixels, pattern: List[HEX], background=BLACK, delay=0.01, iterations=10):
    """moves all the pixels back and forth"""
    for _ in range(iterations):
        swipe_right(pixels, pattern, background, delay)
        swipe_left(pixels, pattern, background, delay)


def _channel_transition(a: int, b: int, count: int) -> Generator[int, None, None]:
    step = (b - a) / count
    for i in range(count):
        yield int(a + step*i)
    yield b


def _color_transition(start: HEX, end: HEX, count: int):
    generators = [_channel_transition(a, b, count) for a, b in zip(start, end)]
    return zip(*generators)


def _multi_transition(pattern: List[HEX], count: int) -> ColorGenerator:
    for a, b in zip(pattern[:-1], pattern[1:]):
        for color in _color_transition(a, b, count):
            yield color


def transition_builder(pattern: List[HEX], count: int) -> Callable[[], ColorGenerator]:
    """returns a function to build new generators"""
    def func() -> ColorGenerator:
        """internal function"""
        return _multi_transition(pattern, count)
    return func


def fade(pixels, pattern: List[HEX], delay=0.1):
    """fades all the colors from start to end"""
    for color in _multi_transition(pattern, 100):
        pixels.fill(color)
        pixels.show()
        time.sleep(delay)


def _iterate_pixels(pixels, iterators: Iterable[Iterator[HEX]]):
    for key, value in enumerate(iterators):
        try:
            pixels[key] = next(value)
        except StopIteration:
            pass


def twinkle(pixels, foreground=WHITE, background=BLACK, delay=0.05, iterations=1000):
    """picks random points and brightens and darkens them"""
    builder = transition_builder([background, foreground, background], 100)

    iterators = [iter([background]) for _ in pixels]

    for i in range(iterations):
        if i % 10 == 0:
            spark = random.randint(0, len(pixels) - 1)
            iterators[spark] = builder()
        _iterate_pixels(pixels, iterators)
        pixels.show()
        time.sleep(delay)
