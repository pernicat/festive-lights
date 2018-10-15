# from colorsys import *

class RGB:
	def __init__(self, *rgb):
		(self.r, self.g, self.b) = rgb
		if len(rgb) > 3:
			self.w = rgb[3]
		else:
			self.w = 0

	def int_values(self, space=255):
		return (round(self.r * space), round(self.g * space), round(self.b * space), round(self.w * space))

	def __int__(self):
		(r, g, b, w) = self.int_values()
		return (w << 24) | (r << 16)| (g << 8) | b