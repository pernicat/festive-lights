"""seasonal functions"""

from festive import tools
from festive import patterns


def christmas(pixels):
    """christmas patters"""
    tools.scroll(pixels, patterns.XMAS_MULTI)
    tools.scroll(pixels, patterns.ICICLE, step=-1)
