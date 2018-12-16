"""seasonal functions"""

from festive import tools
from festive import patterns

# from festive.colors import RED, BLACK


def test(pixels):
    """used to test tools"""
    # tools.swipe(pixels, [RED]*20)
    # tools.fade(pixels, [BLACK, RED])
    tools.twinkle(pixels)


def christmas(pixels):
    """christmas patters"""
    tools.scroll(pixels, patterns.XMAS_MULTI_BIG, delay=0.05, iterations=10)
    tools.twinkle(pixels)
    tools.scroll(pixels, patterns.XMAS_MULTI)
    tools.scroll(pixels, patterns.ICICLE, step=-1)
    tools.twinkle(pixels)
