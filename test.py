import os
import board
import neopixel
from festive import tools
from festive.colors import RED, YELLOW, BLUE, ORANGE, GREEN


LED_COUNT = int(os.getenv('LED_COUNT', 150))

pixels = neopixel.NeoPixel(board.D18, LED_COUNT)

# pixels.fill((0, 255, 0))
tools.pattern_repeater(pixels, [RED, YELLOW, BLUE, ORANGE, GREEN])
