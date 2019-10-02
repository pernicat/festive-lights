from itertools import chain
from datetime import timedelta

from .timing import limit, show_duration
from .transitions import transition
from .effects import scroll, Direction, oscillating_pan
from .sparklemotion import Sparklemotion
from .patterns import RAINBOW, color_wheel, BACKGROUND
from .colors import RED

SHOW_DURATION = timedelta(seconds=10)
REFRESH_RATE = timedelta(seconds=0.02)
SLOW_INTERVAL = timedelta(seconds=0.5)
COLOR_WHEEL = color_wheel()

demo = limit(chain(
    show_duration(Sparklemotion(), SHOW_DURATION),
    show_duration(oscillating_pan([RED] * 12), SHOW_DURATION),
    transition(BACKGROUND, COLOR_WHEEL, SHOW_DURATION),
    limit(scroll(RAINBOW, SHOW_DURATION), SLOW_INTERVAL),
    scroll(COLOR_WHEEL, SHOW_DURATION, Direction.RIGHT),
), REFRESH_RATE)
