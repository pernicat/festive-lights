"""seasonal functions"""
from datetime import date
from enum import Enum

from festive import tools
from festive import patterns


class Events(Enum):
    HALLOWEEN = 1
    CHRISTMAS = 2
    VALENTINES = 3
    SAINT_PATRICK = 4
    EASTER = 5
    # MEMORIAL_DAY = auto()
    INDEPENDENCE_DAY = 7

    SPRING = 10
    SUMMER = 11
    FALL = 12
    WINTER = 13


def get_event_for_date(date_: date) -> Events:
    if date_.month == 10:
        return Events.HALLOWEEN

    # christmas season
    if date_.month == 11 and 20 < date_.day:
        return Events.CHRISTMAS
    if date_.month == 12:
        return Events.CHRISTMAS
    if date_.month == 1 and date_.day < 7:
        return Events.CHRISTMAS

    if date_.month == 2 and 7 < date_.day < 21:
        return Events.VALENTINES

    if date_.month == 3 and 10 < date_.day < 20:
        return Events.SAINT_PATRICK

    if date_.month == 4 and date_.day < 17:
        return Events.EASTER

    if date_.month == 6 and 20 < date_.day:
        return Events.INDEPENDENCE_DAY
    if date_.month == 7 and date_.day < 15:
        return Events.INDEPENDENCE_DAY

    if date_.month in (3, 4, 5):
        return Events.SPRING
    if date_.month in (6, 7, 8):
        return Events.SUMMER
    if date_.month in (9, 10, 11):
        return Events.FALL
    if date_.month in (12, 1, 2):
        return Events.WINTER

    raise Exception("could not find event for '{}'".format(date_.isoformat()))


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
