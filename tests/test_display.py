from unittest import TestCase

from festive.color import black, blue
from festive.display import BaseStrip

class TestBaseStrip(TestCase):
	def test_len(self):
		strip = BaseStrip(5)
		self.assertEqual(len(strip), 5)

	def test_iter(self):
		strip = BaseStrip(4)

		for item in strip:
			self.assertEqual(item, black)
	
	def test_set_get(self):
		strip = BaseStrip(4)

		strip[2] = blue

		self.assertEqual(blue, strip[2])
		self.assertEqual(black, strip[0])