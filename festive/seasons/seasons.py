"""seasonal functions"""
from datetime import date, timedelta, time, datetime
from enum import Enum
from typing import Iterator, Iterable

from festive import tools
from festive import patterns
from festive.timing import until
from festive.seasons.theme import Theme
from festive.colors import (
    HEX, RED, YELLOW, BLUE, ORANGE, GREEN, WHITE, PURPLE, INDIGO, PINK, SKY_BLUE)


DURATION = timedelta(seconds=30)


class Events(Enum):
    HALLOWEEN = 1
    CHRISTMAS = 2
    VALENTINES = 3
    SAINT_PATRICK = 4
    EASTER = 5
    INDEPENDENCE_DAY = 7

    SPRING = 10
    SUMMER = 11
    FALL = 12
    WINTER = 13


EVENT_COLORS = {
    Events.HALLOWEEN: [ORANGE, INDIGO],
    Events.CHRISTMAS: [RED, GREEN, BLUE, YELLOW, WHITE],
    Events.VALENTINES: [RED, PINK],
    Events.SAINT_PATRICK: [GREEN, YELLOW],
    Events.EASTER: [YELLOW, GREEN, PURPLE, WHITE],
    Events.INDEPENDENCE_DAY: [RED, WHITE, BLUE],

    Events.SPRING: [PINK, YELLOW, GREEN, WHITE],
    Events.SUMMER: [ORANGE, WHITE, SKY_BLUE],
    Events.FALL: [RED, ORANGE, YELLOW],
    Events.WINTER: [BLUE, WHITE],
}


def event_for_date(date_: date) -> Events:
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


def theme_for_date(date_: date) -> Theme:
    event = event_for_date(date_)
    colors = EVENT_COLORS[event]
    return Theme(colors=colors, duration=DURATION)


def run() -> Iterable[Iterable[HEX]]:
    while True:
        date_ = date.today()
        tomorrow = datetime.combine(date_, time(0, 0)) + timedelta(days=1)

        theme = theme_for_date(date_)

        for frame in until(theme, tomorrow):
            yield frame


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
