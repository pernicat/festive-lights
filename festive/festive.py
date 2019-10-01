import time
import colorsys
from itertools import islice, cycle, chain
from typing import Union, Any, Iterable, Tuple, NoReturn, NewType, Collection

from festive import seasons, colors
from festive import patterns
from festive.console_demo import ConsoleDemo

Pattern = Collection[colors.HEX]
Frame = Iterable[colors.HEX]
Show = Iterable[Frame]


def color_wheel(length: int) -> Frame:
    step = 1.0 / length

    for i in range(length):
        rgb = colorsys.hsv_to_rgb(step*i, 1.0, 1.0)
        yield colors.rgb_to_hex(rgb)


def scroll(pattern) -> Show:
    while True:
        for i in range(len(pattern)):
            yield cycle(pattern[i:] + pattern[:i])


def add_delay(secs: float, frames: Show) -> Show:
    for item in frames:
        yield item
        time.sleep(secs)


def demo_scroll() -> Show:
    return add_delay(0.5, scroll(patterns.RAINBOW))


def demo_color_wheel() -> Show:
    yield add_delay(0.5, scroll(list(color_wheel(20))))


demo = add_delay(0.5, chain(
    # islice(scroll(patterns.RAINBOW), 10),
    islice(scroll(list(color_wheel(100))), 20)
))


def runner(board: Union[ConsoleDemo, Any], frames: Show) -> NoReturn:
    try:
        for lights in frames:
            for i, color in zip(range(len(board)), lights):
                board[i] = color
            board.show()
    except KeyboardInterrupt:
        return
