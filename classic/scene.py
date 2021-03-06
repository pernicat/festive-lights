import time
import random
from typing import List, Callable, Any

from festive.color import Color
from festive.color import black, red

Colors = List[Color]
Display = Callable[[Colors], Any]



class Growth:
	def __init__(self, length: int, fg=red, bg=black, wait=0.5, growths=1):
		self.fg = fg
		# self.bg = bg
		self.wait = wait
		self.colors = [bg] * length
		self.growths = growths

	def _infect(self, display: Display):
		i = random.randint(0, len(self.colors) - 1)
		self.colors[i] = self.fg
		display(self.colors)
		time.sleep(self.wait)

	def _grow(self, display: Display):
		for i in range(len(self.colors) - 1):
			if self.fg == self.colors[i+1]:
				self.colors[i] = self.fg
		for i in range(len(self.colors) - 1, 1, -1):
			if self.fg == self.colors[i-1]:
				self.colors[i] = self.fg
		display(self.colors)
		time.sleep(self.wait)

	def __call__(self, display: Display):
		while not all(c == self.fg for c in self.colors):
			self._infect(display)
			for _ in range(self.growths):
				self._grow(display)


class Dance:
	def __init__(self, length: int, dance: List[Colors], bg=black, dancers=2, wait=0.3, iterations=4):
		self.length = length
		self.dance = dance
		self.bg = bg
		self.dancers = dancers
		self.wait = wait
		self.iterations = iterations

	def _cell(self, pattern: Colors):
		size = self.length//self.dancers
		left_padding = size//2 - len(pattern)//2
		right_padding = size - len(pattern) - left_padding
		cell = [self.bg]*left_padding + pattern + [self.bg]*right_padding
		return cell

	def _move(self, pattern: Colors, display: Display):
		# print(pattern)
		cell = self._cell(pattern)
		# print(cell)
		joined = cell*self.dancers
		extra = self.length - len(joined)
		# print(joined)
		display(joined + [self.bg]*extra)
		time.sleep(self.wait)

	def _dance(self, display: Display):
		for pattern in self.dance:
			self._move(pattern, display)

	def __call__(self, display: Display):
		for _ in range(self.iterations):
			self._dance(display)