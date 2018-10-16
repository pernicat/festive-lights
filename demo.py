# import time

# from festive.pixel import Pixel
from festive.color import purple, orange, red

from festive.scene import NightRider, Scroll, Growth
from festive.display.console import console

LED_COUNT = 150

nightRider = NightRider(LED_COUNT, [red] * 10 + [orange] * 20)
pumpkinSpice = Scroll(LED_COUNT, [purple] + [orange] * 4, 2)
growth = Growth(LED_COUNT)

# nightRider(console)
# pumpkinSpice(console)
growth(console)

if __name__ == '__main__':

	# wait_ms = 500

	# pixel = Pixel(16)
	# pixel.begin()

	# pixel.show()
	# time.sleep(wait_ms/1000.0)

	# pixel.setPixelColor(0, int(white))
	# pixel.show()
	# time.sleep(wait_ms/1000.0)

	# pixel.setPixelColor(1, int(red))
	# pixel.show()
	# time.sleep(wait_ms/1000.0)

	# pixel.setPixelColor(2, int(green))
	# pixel.show()
	# time.sleep(wait_ms/1000.0)

	# pixel.setPixelColor(3, int(blue))
	# pixel.show()
	# time.sleep(wait_ms/1000.0)



	print("")