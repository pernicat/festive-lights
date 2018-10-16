from typing import Callable, Iterable, List

from festive.color import Color
from festive.color import black

class Controller:
	def __init__(self, length: int, display: Callable[[Iterable[Color]], None]):
		self.colors = [black] * length
		self.display = display
		self.scenes = [] # type: List[object]

	def add_scene(self, scene):
		pass

	def __call__(self):
		pass