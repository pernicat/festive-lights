"""tools unit tests"""

from unittest import TestCase
from festive import tools


class TestColor(TestCase):
	"""test case for tools functions"""

	def test_channel_transition(self):
		"""test color transition function"""
		transition = tools._channel_transition(0, 100, 10)
		for a, b in zip(transition, range(0, 110, 10)):
			assert a == b

	def test_color_transition(self):
		"""test color transition function"""
		transition = tools._color_transition((0, 100, 0), (100, 0, 0), 10)
		expected = [
			(0, 100, 0),
			(10, 90, 0),
			(20, 80, 0),
			(30, 70, 0),
			(40, 60, 0),
			(50, 50, 0),
			(60, 40, 0),
			(70, 30, 0),
			(80, 20, 0),
			(90, 10, 0),
			(100, 0, 0),
		]
		for a, b in zip(transition, expected):
			assert a == b
