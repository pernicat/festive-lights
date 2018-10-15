import unittest
from festive.color import RGB

class TestColor(unittest.TestCase):
	def test_int_values(self):
		color = RGB(0.0, 0.5, 1.0)
		(r, g, b, w) = color.int_values()
		self.assertEqual(0, r)
		self.assertEqual(128, g)
		self.assertEqual(255, b)
		self.assertEqual(0, w)

	def test_cast_int(self):
		black = RGB(0.0, 0.0, 0.0)

		self.assertEqual(0, int(black))

		white = RGB(1.0, 1.0, 1.0)

		self.assertEqual(16777215, int(white))

		color = RGB(0.0, 0.5, 1.0)

		self.assertEqual(33023, int(color))