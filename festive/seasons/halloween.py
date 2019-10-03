from itertools import chain
from datetime import timedelta
from typing import List

from festive.timing import limit, show_duration
from festive.transitions import transition, chain_fill_transitions
from festive.effects import scroll, Direction, oscillating_pan

from festive.patterns import SPOOKY_THEME, spacing, widen
from festive.colors import RED, HEX

SCROLL_INTERVAL = timedelta(seconds=0.3)

# SHOW_DURATION = timedelta(seconds=10)
# REFRESH_RATE = timedelta(seconds=0.02)
#
# COLOR_WHEEL = color_wheel()
#
# demo = limit(chain(
#     show_duration(Sparklemotion(), SHOW_DURATION),
#     show_duration(oscillating_pan([RED] * 12), SHOW_DURATION),
#     transition(BACKGROUND, COLOR_WHEEL, SHOW_DURATION),
#     limit(scroll(RAINBOW, SHOW_DURATION), SLOW_INTERVAL),
#     scroll(COLOR_WHEEL, SHOW_DURATION, Direction.RIGHT),
# ), REFRESH_RATE)


def halloween(scene_duration: timedelta):
    def limit_scroll(colors: List[HEX]):
        return limit(scroll(colors, scene_duration), SCROLL_INTERVAL)

    return chain(
        limit_scroll(spacing(SPOOKY_THEME, 4)),
        limit_scroll(widen(SPOOKY_THEME, 8)),
        limit_scroll(SPOOKY_THEME),
        chain_fill_transitions(SPOOKY_THEME, scene_duration),
    )
