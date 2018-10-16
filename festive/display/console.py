import sys
from typing import Iterable

from festive.color import Color

def console(colors: Iterable[Color]):
	output = ""
	for color in colors:
		output+="\033[48;2;%d;%d;%dm \033[0m" % color.rgb_values()[:3]

	sys.stdout.write("\r" + output)