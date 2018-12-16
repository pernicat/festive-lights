"""Color pattern constants"""

from typing import List

from festive.colors import Color, RED, YELLOW, BLUE, ORANGE, GREEN, WHITE

Pattern = List[Color]

BIG = 10

XMAS_MULTI = [RED, YELLOW, BLUE, ORANGE, GREEN]
"""red, yellow, blue, orange, green"""
XMAS_MULTI_BIG = [RED]*BIG + [YELLOW]*BIG + [BLUE]*BIG + [ORANGE]*BIG + [GREEN]*BIG
"""red, yellow, blue, orange, green"""

ICICLE = [BLUE] + [WHITE]*4
"""blue, white*4"""
