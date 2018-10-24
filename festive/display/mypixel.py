from typing import Iterable

from festive.color import Color
from neopixel import NeoPixel


class MyPixel(NeoPixel):
	def __call__(self, colors: Iterable[Color]) -> None:
		if len(colors) is not self.numPixels():
			raise Exception('Number of pixels must match colors')
		for index, color in enumerate(colors):
			self.setPixelColorRGB(index, int(color))
