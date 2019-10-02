import time
import colorsys
from datetime import datetime, timedelta
from itertools import islice, cycle, chain
from typing import Union, Any, Iterable, Tuple, NewType, List

from festive import seasons, colors, patterns
from festive.types import Frame, Pattern, Show, Transition
from festive.console_demo import ConsoleDemo











def runner(board: Union[ConsoleDemo, Any], frames: Show):
    try:
        for lights in frames:
            for i, color in zip(range(len(board)), lights):
                board[i] = color
            board.show()
    except KeyboardInterrupt:
        return
