from itertools import chain
from datetime import timedelta

from festive.timing import limit, show_duration
from festive.transitions import transition, chain_fill_transitions
from festive.effects import scroll, Direction, oscillating_pan

from festive.patterns import SPOOKY1
from festive.colors import RED

# SHOW_DURATION = timedelta(seconds=10)
# REFRESH_RATE = timedelta(seconds=0.02)
# SLOW_INTERVAL = timedelta(seconds=0.5)
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
    return chain(
        chain_fill_transitions(SPOOKY1, scene_duration)
    )
