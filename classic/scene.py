import time
import random
from typing import List, Callable, Any

from festive.color import Color
from festive.color import black, red

Colors = List[Color]
Display = Callable[[Colors], Any]


class NightRider:
	def __init__(self, length: int, pattern: Colors, bg=black, wait=0.01, width=30, iterations=10):
		self.length = length
		self.pattern = pattern
		self.bg = bg
		self.wait = wait
		self.iterations = iterations

	def _pos_to_list(self, index: int) -> Colors:
		pre = [self.bg] * index
		post = [self.bg] * (self.length - len(self.pattern) - index)
		return pre + self.pattern + post
	
	def _right(self, display: Display):
		for i in range(self.length - len(self.pattern)):
			display(self._pos_to_list(i))
			time.sleep(self.wait)

	def _left(self, display: Display):
		for i in range(self.length - len(self.pattern), 0, -1):
			display(self._pos_to_list(i))
			time.sleep(self.wait)

	def __call__(self, display: Display):
		for _ in range(self.iterations):
			self._right(display)
			self._left(display)


class Scroll:
	def __init__(self, length: int, pattern: Colors, step=1, wait=0.5, iterations=10):
		self.length = length
		self.pattern = pattern
		self.step = step
		self.wait = wait
		self.iterations = iterations

	def _scroll(self, display: Display):
		remander = self.pattern * (self.length // len(self.pattern) + 1) 

		if self.step > 0:
			r = range(0, len(self.pattern), self.step)
		else:
			r = range(len(self.pattern), 0, self.step)

		for l in r:
			colors = self.pattern[l:] + remander

			display(colors[:self.length])
			time.sleep(self.wait)

	def __call__(self, display: Display):
		for _ in range(self.iterations):
			self._scroll(display)


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