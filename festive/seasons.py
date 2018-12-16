"""seasonal functions"""

from festive import tools
from festive import patterns

from festive.colors import RED


def test(pixels):
    """used to test tools"""
    tools.swipe(pixels, [RED]*20)


def christmas(pixels):
    """christmas patters"""
    tools.scroll(pixels, patterns.XMAS_MULTI)
    tools.scroll(pixels, patterns.ICICLE, step=-1)
