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
        total_seconds = sleep_delta.total_seconds()
        if total_seconds <= 0:
            continue
        time.sleep(total_seconds)


def until(frames: Iterable[Iterable[HEX]], datetime_: datetime) -> Iterable[Iterable[HEX]]:
    for frame in frames:
        if datetime.now() > datetime_:
            break

        yield frame


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


def show_duration(show: Iterable[Iterable[HEX]], duration: timedelta) -> Iterable[Iterable[HEX]]:
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
