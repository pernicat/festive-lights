from itertools import islice
from typing import List, Iterable, NewType

from .colors import HEX

from config import Config

Pattern = NewType('Pattern', List[HEX])
Frame = NewType('Frame', Iterable[HEX])
Show = NewType('Show', Iterable[Frame])
Transition = NewType('Transition', List[Iterable[HEX]])


def frame_to_pattern(frame: Frame) -> Pattern:
    return list(islice(frame, Config.LED_COUNT))
