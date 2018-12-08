import os
import time
from festive.console_demo import ConsoleDemo
from festive import tools
from festive.colors import red, yellow, blue, orange, green

LED_COUNT = int(os.getenv('LED_COUNT', 150))

pixels = ConsoleDemo(None, LED_COUNT)
pixels.show()
pixels.fill((0, 255, 0))
time.sleep(1.0)
tools.pattern_repeater(pixels, [red, yellow, blue, orange, green])
print('')


# # import time
#
# # from festive.pixel import Pixel
# from festive.color import purple, orange, red
# from festive.seasons import Halloween
#
# from festive.scene import NightRider, Scroll, Growth
# from festive.display.console import console
#
# LED_COUNT = 150
#
# halloween = Halloween(LED_COUNT)
#
# if __name__ == '__main__':
#
# 	for scene in halloween:
# 		scene(console)
#
# 	print("")
