import os
import board
import neopixel


LED_COUNT = int(os.getenv('LED_COUNT', 150))

pixels = neopixel.NeoPixel(board.D18, LED_COUNT)

pixels.fill((0, 255, 0))
