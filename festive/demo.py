from itertools import chain
from datetime import timedelta

from .timing import limit, run_time
from .transitions import transition
from .effect import scroll_right, scroll_left
from .patterns import RAINBOW, color_wheel, fill
from .colors import BLACK

BACKGROUND = fill(BLACK)

DEMO_INTERVAL = timedelta(seconds=10)
STEP_INTERVAL = timedelta(seconds=0.1)
COLOR_WHEEL = color_wheel()

demo = limit(chain(
    transition(BACKGROUND, COLOR_WHEEL, DEMO_INTERVAL),
    run_time(scroll_right(RAINBOW), DEMO_INTERVAL),
    run_time(scroll_left(COLOR_WHEEL), DEMO_INTERVAL)
), STEP_INTERVAL)
