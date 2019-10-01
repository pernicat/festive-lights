"""Color constants"""

from typing import Tuple, NamedTuple


RGB = NamedTuple('RGB', [('red', float), ('green', float), ('blue', float)])

HEX = NamedTuple('HEX', [('red', int), ('green', int), ('blue', int)])


def hex_to_rgb(hex_: HEX) -> RGB:
    return RGB(*(v/255 for v in hex_))


def rgb_to_hex(rgb: RGB) -> HEX:
    return HEX(*(round(c * 255) for c in rgb))


BLACK = HEX(0, 0, 0)
WHITE = HEX(255, 255, 255)

RED = HEX(255, 0, 0)
GREEN = HEX(0, 255, 0)
BLUE = HEX(0, 0, 255)

YELLOW = HEX(255, 255, 0)
CYAN = HEX(0, 255, 255)
MAGENTA = HEX(255, 0, 255)

ORANGE = HEX(255, 127, 0)
PURPLE = HEX(127, 0, 127)

INDIGO = HEX(68, 0, 255)
