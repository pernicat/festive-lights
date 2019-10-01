"""Color pattern constants"""

from typing import List, Iterable

from festive.colors import HEX, RED, YELLOW, BLUE, ORANGE, GREEN, WHITE

Pattern = List[HEX]

BIG = 10

XMAS_MULTI = [RED, YELLOW, BLUE, ORANGE, GREEN]
"""red, yellow, blue, orange, green"""
XMAS_MULTI_BIG = [RED]*BIG + [YELLOW]*BIG + [BLUE]*BIG + [ORANGE]*BIG + [GREEN]*BIG
"""red, yellow, blue, orange, green"""

RAINBOW = [RED, ORANGE, YELLOW, GREEN, BLUE]

ICICLE = [BLUE] + [WHITE]*4
"""blue, white*4"""
