"""Color pattern constants"""

from typing import List

from festive.colors import Color, RED, YELLOW, BLUE, ORANGE, GREEN, WHITE

Pattern = List[Color]

XMAS_MULTI = [RED, YELLOW, BLUE, ORANGE, GREEN]
"""red, yellow, blue, orange, green"""
ICICLE = [BLUE] + [WHITE]*4
"""blue, white*4"""
