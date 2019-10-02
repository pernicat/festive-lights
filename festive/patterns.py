"""Color pattern constants"""
from colorsys import hsv_to_rgb
from typing import Iterable, List, NewType, Any
from itertools import cycle, islice

from .colors import HEX, RED, YELLOW, BLUE, ORANGE, GREEN, WHITE, PURPLE, BLACK, INDIGO, rgb_to_hex
from .types import frame_to_pattern

from config import Config

T = NewType("T", Any)

# Christmas
BIG = 10

XMAS_MULTI = [RED, YELLOW, BLUE, ORANGE, GREEN]
"""red, yellow, blue, orange, green"""
XMAS_MULTI_BIG = [RED]*BIG + [YELLOW]*BIG + [BLUE]*BIG + [ORANGE]*BIG + [GREEN]*BIG
"""red, yellow, blue, orange, green"""

RAINBOW = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
"""standard rainbow colors"""

ICICLE = [BLUE] + [WHITE]*4
"""blue, white*4"""

# Halloween
SPOOKY1 = [ORANGE, RED, BLACK, INDIGO, GREEN]
SPOOKY2 = [ORANGE, INDIGO, RED, PURPLE]


def flatten(tall: List[List[T]]) -> List[T]:
    return [item for sub in tall for item in sub]


def spacing(colors: List[HEX], padding: int, background: HEX = BLACK) -> List[HEX]:
    return flatten([[c] + padding*[background] for c in colors])


def widen(colors: List[HEX], amount: int) -> List[HEX]:
    return flatten([amount*[c] for c in colors])


def _color_wheel(length: int) -> Iterable[HEX]:
    step = 1.0 / length

    for i in range(length):
        rgb = hsv_to_rgb(step*i, 1.0, 1.0)
        yield rgb_to_hex(rgb)


def color_wheel(length: int = Config.LED_COUNT) -> List[HEX]:
    return frame_to_pattern(_color_wheel(length))


def fill(color: HEX, length: int = Config.LED_COUNT) -> List[HEX]:
    return list(islice(cycle([color]), length))


BACKGROUND = fill(BLACK)
