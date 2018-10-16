from abc import abstractmethod

from festive.color import black
from festive.color import Color



class BaseStrip:
	def __init__(self, length: int):
		self.data = [black] * length
		self.index = 0

	def __len__(self) -> int: 
		return len(self.data)

	def __iter__(self):
		return self
	
	def __next__(self) -> Color:
		try:
			value = self[self.index]
			self.index+= 1
			return value
		except IndexError:
			raise StopIteration

	def __getitem__(self, key: int) -> Color:
		return self.data[key]

	def __setitem__(self, key: int, value: Color) -> None:
		self.data[key] = value
	
	@abstractmethod
	def show(self) -> None:
		pass