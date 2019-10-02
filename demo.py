#!/usr/bin/env python3
"""Runs a demo of the LEDs on the command line"""

from festive.festive import runner
from festive.demo import demo
from festive.console_demo import ConsoleDemo

from config import Config


def main():
    """Main function to run demo"""
    pixels = ConsoleDemo(None, Config.LED_COUNT, auto_write=False)
    # seasons.test(pixels)
    # seasons.christmas(pixels)

    runner(pixels, demo)

    print('')


if __name__ == "__main__":
    main()
