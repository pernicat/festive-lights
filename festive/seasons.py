from festive import tools
from festive import patterns


def christmas(pixels):
    tools.scroll(pixels, patterns.christmas_multicolor)
    tools.scroll(pixels, patterns.winter, step=-1)
