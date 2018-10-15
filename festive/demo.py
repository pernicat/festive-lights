from color import RGB

class Pixel:
	def __init__(self, num):
		self._led_data = [0] * num


	def begin(self):
		"""Initialize library, must be called once before other functions are
		called.
		"""
		# return

	def show(self):
		"""Update the display with the data from the LED buffer."""
		# TODO
		output = ""
		for color in self._led_data:
		#for color in range(16, 256):
			#c = ((color & 0xf00000) >> 12) | ((color & 0xf000) >> 8) | ((color & 0xf0) >> 4)
			#c = ((color & 0xe00000) >> 16) | ((color & 0xe000) >> 11) | ((color & 0xc0) >> 6)
			r = (color & 0xff0000) >> 16
			g = (color & 0xff00) >> 8
			b = color & 0xff
			output+="\033[48;2;%d;%d;%dm \033[0m" % (r, g, b)

		print(output)

	def setPixelColor(self, n, color):
		"""Set LED at position n to the provided 24-bit color value (in RGB order).
		"""
		self._led_data[n] = color

	def setPixelColorRGB(self, n, red, green, blue, white = 0):
		"""Set LED at position n to the provided red, green, and blue color.
		Each color component should be a value from 0 to 255 (where 0 is the
		lowest intensity and 255 is the highest intensity).
		"""
		# self.setPixelColor(n, Color(red, green, blue, white))

	def setBrightness(self, brightness):
		"""Scale each LED in the buffer by the provided brightness.  A brightness
		of 0 is the darkest and 255 is the brightest.
		"""
		# TODO
		# return

	def getBrightness(self):
		"""Get the brightness value for each LED in the buffer. A brightness
		of 0 is the darkest and 255 is the brightest.
		"""
		# TODO
		return 255

	def getPixels(self):
		"""Return an object which allows access to the LED display data as if
		it were a sequence of 24-bit RGB values.
		"""
		return self._led_data

	def numPixels(self):
		"""Return the number of pixels in the display."""
		return len(self._led_data)

	def getPixelColor(self, n):
		"""Get the 24-bit RGB color value for the LED at position n."""
		return self._led_data[n]

if __name__ == '__main__':
	pixel = Pixel(16)
	pixel.begin()
	pixel.setPixelColor(0, int(RGB(1.0, 1.0, 1.0)))
	pixel.setPixelColor(1, int(RGB(1.0, 0.0, 0.0)))
	pixel.setPixelColor(2, int(RGB(0.0, 1.0, 0.0)))
	pixel.setPixelColor(3, int(RGB(0.0, 0.0, 1.0)))
	pixel.show()
