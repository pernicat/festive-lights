import time
from datetime import datetime, timedelta
from typing import Iterable

from .colors import HEX


def limit(frames: Iterable[Iterable[HEX]], interval: timedelta) -> Iterable[Iterable[HEX]]:
    """
    Limits the speed of each frame

    :param frames: input
    :param interval: amount of time between each frame
    :return: output limited by time
    """
    for item in frames:
        stop = datetime.now() + interval
        yield item
        sleep_delta = stop - datetime.now()
        time.sleep(sleep_delta.total_seconds())


def elapsed(duration: timedelta) -> Iterable[timedelta]:
    """
    Generates a list of time intervals since the generator was started

    :param duration: total amount of time this should run
    :return: an iterable object of timedeltas
    """
    start = datetime.now()

    while True:
        elapsed_ = datetime.now() - start

        if elapsed_ > duration:
            break

        yield elapsed_


def elapsed_fraction(duration: timedelta) -> Iterable[float]:
    """
    Similar to elapsed but returns the value as a faction of how much of the interval has elapsed

    :param duration: interval: total amount of time this should run
    :return: an iterable object of floats
    """
    for elapsed_ in elapsed(duration):
        yield elapsed_ / duration


def run_time(show: Iterable[Iterable[HEX]], duration: timedelta) -> Iterable[Iterable[HEX]]:
    """
    Limits the total amount of time this show should run
    
    :param show: 
    :param duration: 
    :return: 
    """
    start = datetime.now()
    end = start + duration

    for frame in show:
        if end <= datetime.now():
            break
        yield frame
