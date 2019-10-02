"""Various types of transitions from color to color"""
from datetime import timedelta
from itertools import islice, cycle
from typing import List, Iterable, Tuple

from .tools import transform_to_show
from .colors import RGB, HEX, hex_to_rgb, rgb_to_hex
from .timing import elapsed_fraction
from .patterns import fill


def transition_step(start: RGB, end: RGB, scale: float) -> RGB:
    diff = tuple(e - s for s, e in zip(start, end))
    deltas = tuple(d*scale for d in diff)

    return tuple(round(s + d, 3) for s, d in zip(start, deltas))


def _rgb_diff(start: RGB, end: RGB) -> Tuple[float, ...]:
    return tuple(e - s for s, e in zip(start, end))


def rgb_step_transition(start: RGB, end: RGB, length: int) -> Iterable[RGB]:
    diff = _rgb_diff(start, end)

    # how much each channel needs to change for each step of the transition
    deltas = tuple(d / length for d in diff)

    for i in range(length):
        yield tuple(round(s + d*i, 3) for s, d in zip(start, deltas))


def rgb_timed_transition(start: RGB, end: RGB, duration: timedelta) -> Iterable[RGB]:
    diff = _rgb_diff(start, end)

    for frac in elapsed_fraction(duration):
        yield tuple(round(s + d*frac, 3) for s, d in zip(start, diff))


def hex_step_transition(start: HEX, end: HEX, length: int) -> Iterable[HEX]:
    for rgb in rgb_step_transition(
            hex_to_rgb(start), hex_to_rgb(end), length):
        yield rgb_to_hex(rgb)


def hex_timed_transition(start: HEX, end: HEX, duration: timedelta) -> Iterable[HEX]:
    for rgb in rgb_timed_transition(
            hex_to_rgb(start), hex_to_rgb(end), duration):
        yield rgb_to_hex(rgb)


def _match_lengths(*items: List[HEX]) -> Tuple[Iterable[HEX], ...]:
    lengths = tuple(len(i) for i in items)
    if 0 in lengths:
        raise Exception("Can't transition pattern with length of 0")
    max_length = max(lengths)

    return tuple(islice(cycle(i), max_length) for i in items)


def step_transition(start: List[HEX], end: List[HEX], length: int) -> List[Iterable[HEX]]:
    matched = _match_lengths(start, end)

    return [hex_step_transition(s, e, length) for s, e in zip(*matched)]


def timed_transition(start: List[HEX], end: List[HEX], duration: timedelta) -> List[Iterable[HEX]]:
    matched = _match_lengths(start, end)

    return [hex_timed_transition(s, e, duration) for s, e in zip(*matched)]


def transition(start: List[HEX], end: List[HEX], duration: timedelta) -> Iterable[Iterable[HEX]]:
    return transform_to_show(timed_transition(start, end, duration))


def chain_fill_transitions(colors: List[HEX], duration: timedelta) -> Iterable[Iterable[HEX]]:
    if len(colors) < 2:
        raise Exception("must be at least 2 colors to chain a transition")

    step_dur = duration / (len(colors)-1)

    fills = [fill(c) for c in colors]

    for a, b in zip(fills[:-1], fills[1:]):
        for colors in transition(a, b, step_dur):
            yield colors
