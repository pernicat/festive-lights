from itertools import chain
from datetime import timedelta

from .timing import limit, show_duration
from .transitions import transition
from .effects import scroll, Direction, oscillating_pan
from .effects.sparklemotion import Sparklemotion
from .patterns import RAINBOW, color_wheel, BACKGROUND, SPOOKY_THEME, FREEDOM_THEME
from .colors import RED
from .seasons import halloween, Theme, run

SCENE_DURATION = timedelta(seconds=10)
REFRESH_RATE = timedelta(seconds=0.05)
SLOW_INTERVAL = timedelta(seconds=0.5)
COLOR_WHEEL = color_wheel()

# demo = limit(chain(
#     Theme(FREEDOM_THEME, SCENE_DURATION),
#     Theme(SPOOKY_THEME, SCENE_DURATION),
#     halloween(4*SCENE_DURATION),
#     show_duration(Sparklemotion(), SCENE_DURATION),
#     show_duration(oscillating_pan([RED] * 12), SCENE_DURATION),
#     transition(BACKGROUND, COLOR_WHEEL, SCENE_DURATION),
#     limit(scroll(RAINBOW, SCENE_DURATION), SLOW_INTERVAL),
#     scroll(COLOR_WHEEL, SCENE_DURATION, Direction.RIGHT),
# ), REFRESH_RATE)

demo = limit(run(), REFRESH_RATE)
