#!/usr/bin/env python3
"""runs the neopixels"""

import os
import board
import neopixel
from festive import seasons


LED_COUNT = int(os.getenv('LED_COUNT', '150'))


def main():
    """runs the neopixels"""
    pixels = neopixel.NeoPixel(board.D18, LED_COUNT, auto_write=False)

    while True:
        seasons.christmas(pixels)


if __name__ == "__main__":
    main()
