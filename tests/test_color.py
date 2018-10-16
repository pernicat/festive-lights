from unittest import TestCase
from festive.color import Color

class TestColor(TestCase):
	def test_int_values(self):
		color = Color(0.0, 0.5, 1.0)
		(r, g, b, w) = color.rgb_values()
		self.assertEqual(0, r)
		self.assertEqual(128, g)
		self.assertEqual(255, b)
		self.assertEqual(0, w)

	def test_cast_int(self):
		black = Color(0.0, 0.0, 0.0)

		self.assertEqual(0, int(black))

		white = Color(1.0, 1.0, 1.0)

		self.assertEqual(16777215, int(white))

		color = Color(0.0, 0.5, 1.0)

		self.assertEqual(33023, int(color))