#!/usr/bin/env python3
"""runs the neopixels"""

import board
import neopixel
from festive.festive import runner
from festive.demo import demo

from config import Config


def main():
    """runs the neopixels"""
    pixels = neopixel.NeoPixel(board.D18, Config.LED_COUNT, auto_write=False)

    runner(pixels, demo)


if __name__ == "__main__":
    main()
