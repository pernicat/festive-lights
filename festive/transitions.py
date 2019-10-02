from typing import Iterable
from itertools import islice, cycle, chain

from .types import Transition, Pattern, Show
from .colors import RGB, HEX, hex_to_rgb, rgb_to_hex


def transition_step(start: RGB, end: RGB, scale: float) -> RGB:
    diff = tuple(e - s for s, e in zip(start, end))
    deltas = tuple(d*scale for d in diff)

    return tuple(round(s + d, 3) for s, d in zip(start, deltas))


def rgb_color_transition(start: RGB, end: RGB, length: int) -> Iterable[RGB]:
    diff = tuple(e-s for s, e in zip(start, end))

    # how much each channel needs to change for each step of the transition
    deltas = tuple(d / length for d in diff)

    for i in range(length):
        yield tuple(round(s + d*i, 3) for s, d in zip(start, deltas))


def hex_color_transition(start: HEX, end: HEX, length: int) -> Iterable[HEX]:
    for rgb in rgb_color_transition(
            hex_to_rgb(start), hex_to_rgb(end), length):
        yield rgb_to_hex(rgb)


def transition(start: Pattern, end: Pattern, length: int) -> Transition:
    lengths = (len(start), len(end))
    if 0 in lengths:
        raise Exception("Can't transition pattern with length of 0 start: {}, end: {}".format(*lengths))
    pattern_length = max(lengths)

    # duplicates the short list so it is the same length as the longer list
    start = list(islice(cycle(start), pattern_length))
    end = list(islice(cycle(end), pattern_length))

    return [hex_color_transition(s, e, length) for s, e in zip(start, end)]


def transition_to_show(transitions: Transition) -> Show:
    iterables = [iter(t) for t in transitions]

    while True:
        try:
            yield [next(i) for i in iterables]
        except StopIteration:
            break
