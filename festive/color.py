# from colorsys import *
from typing import Tuple
from abc import abstractmethod


class Color:
	def __init__(self, r: float, g: float, b: float, w: float=0.0):
		self.r = r
		self.g = g
		self.b = b
		self.w = w

	def to_tuple(self) -> Tuple[float, float, float]:
		return self.r, self.g, self.b

	def rgb_values(self, bits: int=8) -> Tuple[int, int, int, int]:
		space = 2 ** 8 - 1
		return round(self.r * space), round(self.g * space), round(self.b * space), round(self.w * space)

	def __int__(self) -> int:
		(r, g, b, w) = self.rgb_values()
		return (w << 24) | (r << 16) | (g << 8) | b

	def __repr__(self) -> str:
		return "Color(%d, %d, %d)" % self.to_tuple()


black = Color(0.0, 0.0, 0.0)
white = Color(1.0, 1.0, 1.0)

red = Color(1.0, 0.0, 0.0)
green = Color(0.0, 1.0, 0.0)
blue = Color(0.0, 0.0, 1.0)

yellow = Color(1.0, 1.0, 0.0)
cyan = Color(0.0, 1.0, 1.0)
magenta = Color(1.0, 0.0, 1.0)

orange = Color(1.0, 0.5, 0.0)
purple = Color(0.5, 0.0, 0.5)

indigo = Color(0.267, 0.0, 1.0)