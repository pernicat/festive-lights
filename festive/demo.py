from itertools import chain
from datetime import timedelta

from .timing import limit, run_time
from .transitions import transition_to_show, transition
from .effect import scroll_right, scroll_left
from .patterns import RAINBOW, color_wheel

DEMO_INTERVAL = timedelta(seconds=10)
STEP_INTERVAL = timedelta(seconds=0.1)
COLOR_WHEEL = color_wheel()

demo = limit(chain(
    run_time(transition_to_show(transition(RAINBOW, COLOR_WHEEL, 30)), DEMO_INTERVAL),
    run_time(scroll_right(RAINBOW), DEMO_INTERVAL),
    run_time(scroll_left(COLOR_WHEEL), DEMO_INTERVAL)
), STEP_INTERVAL)
