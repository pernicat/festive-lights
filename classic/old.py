from festive.color import purple, red, orange, white, green


def skeleton_dance():
	size = 12
	moves = 8

	x = white
	o = black

	move_a = [x, x, o, x, x]
	move_b = [x, o, x, o, x]

	space = [o]*size

	dance_left  = [move_a+space, move_b+space]*moves
	dance_right = [space+move_a, space+move_b]*moves

	slide_right = [space[:i] + move_b + space[i:] for i, _ in enumerate(space)]
	slide_left  = [space[i:] + move_b + space[:i] for i, _ in enumerate(space)]

	return dance_left + slide_right + dance_right + slide_left


monster = [purple]*3 + [white] + [purple]*5 + [white] + [purple]*3
pumpkin_spice = [purple] + [orange]*4
spooky = [red, orange, green, purple]


def Halloween(count: int):
	return [
		Dance(count, skeleton_dance(), dancers=4),
		Scroll(count, spooky, 1),
		Scroll(count, spooky, -1),
		NightRider(count, monster),
		Scroll(count, pumpkin_spice, 1),
		Scroll(count, pumpkin_spice, -1),
		Growth(count),
	]

from festive.color import purple, red, orange, white, green, black

from classic.scene import NightRider, Scroll, Growth, Dance


def skeleton_dance():
	size = 12
	moves = 8

	x = white
	o = black

	move_a = [x, x, o, x, x]
	move_b = [x, o, x, o, x]

	space = [o]*size

	dance_left  = [move_a+space, move_b+space]*moves
	dance_right = [space+move_a, space+move_b]*moves

	slide_right = [space[:i] + move_b + space[i:] for i, _ in enumerate(space)]
	slide_left  = [space[i:] + move_b + space[:i] for i, _ in enumerate(space)]

	return dance_left + slide_right + dance_right + slide_left


monster = [purple]*3 + [white] + [purple]*5 + [white] + [purple]*3
pumpkin_spice = [purple] + [orange]*4
spooky = [red, orange, green, purple]


def Halloween(count: int):
	return [
		Dance(count, skeleton_dance(), dancers=4),
		Scroll(count, spooky, 1),
		Scroll(count, spooky, -1),
		NightRider(count, monster),
		Scroll(count, pumpkin_spice, 1),
		Scroll(count, pumpkin_spice, -1),
		Growth(count),
	]

#!/usr/bin/env python3
# @see https://github.com/jgarff/rpi_ws281x/blob/master/python/examples/strandtest.py
# Direct port of the Arduino MyPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
import argparse
from festive.display.mypixel import MyPixel
from classic.seasons import Halloween

# LED strip configuration:
LED_COUNT      = 150     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

halloween = Halloween(LED_COUNT)

def pumpkinSpice(strip, fg, bg, wait_ms=300, iterations=20, width=10):
    """Orange with wipping green"""
    for _ in range(iterations):
        for i in range(width):
            for j in range(strip.numPixels()):
                if 0 == (j+i)%width:
                    strip.setPixelColor(j, fg)
                else:
                    strip.setPixelColor(j, bg)
            strip.show()
            time.sleep(wait_ms/1000.0)


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def nightRider(strip, fg, bg, wait_ms=10, width=30, iterations=10):
    """1980s AI"""
    for j in range(iterations):
        for i in range(strip.numPixels() - width):
            for q in range(strip.numPixels()):
                if i < q < i+width:
                    strip.setPixelColor(q, fg)
                else:
                    strip.setPixelColor(q, bg)
            strip.show()
            time.sleep(wait_ms/1000.0)
        for i in range(strip.numPixels() - width, 0, -1):
            for q in range(strip.numPixels()):
                if i < q < i+width:
                    strip.setPixelColor(q, fg)
                else:
                    strip.setPixelColor(q, bg)
            strip.show()
            time.sleep(wait_ms/1000.0)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create MyPixel object with appropriate configuration.
    strip = MyPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            for scene in halloween:
                scene(strip)
            # print ('Color wipe animations.')
            # colorWipe(strip, Color(255, 0, 0))  # Red wipe
            # colorWipe(strip, Color(0, 255, 0))  # Blue wipe
            # colorWipe(strip, Color(0, 0, 255))  # Green wipe
            # print ('Theater chase animations.')
            # theaterChase(strip, Color(127, 127, 127))  # White theater chase
            # theaterChase(strip, Color(127,   0,   0))  # Red theater chase
            # theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
            # print ('Rainbow animations.')
            # rainbow(strip)
            # rainbowCycle(strip)
            # theaterChaseRainbow(strip)
            # print ('Pumpkin Spice')
            # pumpkinSpice(strip, Color(0, 128, 128), Color(20, 150, 00))
            # print ('Red Color Wipe')
            # colorWipe(strip, Color(255, 0, 0), 100)  # Red wipe
            # print ('Rainbow Slow')
            # rainbowCycle(strip, 100, 20)
            # print ('Night Rider')
            # nightRider(strip, Color(0, 255, 0), Color(0, 0, 0))


    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
