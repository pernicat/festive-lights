import time
from datetime import datetime, timedelta
from typing import Iterable

from festive.types import Show


def limit(frames: Show, interval: timedelta) -> Show:
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


def elapsed(interval: timedelta) -> Iterable[timedelta]:
    """
    Generates a list of time intervals since the generator was started

    :param interval: total amount of time this should run
    :return: an iterable object of timedeltas
    """
    start = datetime.now()

    while True:
        elapsed_ = datetime.now() - start

        if elapsed_ > interval:
            break

        yield elapsed_


def elapsed_fraction(interval: timedelta) -> Iterable[float]:
    """
    Similar to elapsed but returns the value as a faction of how much of the interval has elapsed

    :param interval: interval: total amount of time this should run
    :return: an iterable object of floats
    """
    for elapsed_ in elapsed(interval):
        yield elapsed_ / interval


def run_time(show: Show, delta: timedelta) -> Show:
    """
    Limits the total amount of time this show should run
    
    :param show: 
    :param delta: 
    :return: 
    """
    start = datetime.now()
    end = start + delta

    for frame in show:
        if end <= datetime.now():
            break
        yield frame
