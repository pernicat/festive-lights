#!/usr/bin/env python3
"""Runs a demo of the LEDs on the command line"""

import os
from festive.console_demo import ConsoleDemo
from festive import seasons

LED_COUNT = int(os.getenv('LED_COUNT', '150'))


def main():
    """Main function to run demo"""
    pixels = ConsoleDemo(None, LED_COUNT, auto_write=False)
    # seasons.test(pixels)
    seasons.christmas(pixels)
    print('')


if __name__ == "__main__":
    main()
