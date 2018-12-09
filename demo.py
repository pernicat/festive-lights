import os
from festive.console_demo import ConsoleDemo
from festive import seasons

LED_COUNT = int(os.getenv('LED_COUNT', 150))

pixels = ConsoleDemo(None, LED_COUNT, auto_write=False)

seasons.christmas(pixels)

print('')
