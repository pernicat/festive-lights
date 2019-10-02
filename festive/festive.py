from typing import Union, Any, Iterable

from .colors import HEX
from .console_demo import ConsoleDemo


def runner(board: Union[ConsoleDemo, Any], show: Iterable[Iterable[HEX]]):
    try:
        for lights in show:
            for i, color in zip(range(len(board)), lights):
                board[i] = color
            board.show()
    except KeyboardInterrupt:
        return
