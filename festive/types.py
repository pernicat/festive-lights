from itertools import islice
from typing import List, Iterable, NewType

from .colors import HEX

from config import Config


def frame_to_pattern(frame: Iterable[HEX]) -> List[HEX]:
    return list(islice(frame, Config.LED_COUNT))
