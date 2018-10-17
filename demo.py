# import time

# from festive.pixel import Pixel
from festive.color import purple, orange, red
from festive.seasons import Halloween

from festive.scene import NightRider, Scroll, Growth
from festive.display.console import console

LED_COUNT = 150

halloween = Halloween(LED_COUNT)

if __name__ == '__main__':

	for scene in halloween:
		scene(console)

	print("")