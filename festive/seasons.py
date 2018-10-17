from festive.color import purple, orange, red, orange, white, green, black

from festive.scene import NightRider, Scroll, Growth, Dance

def skeleton_dance():
	size = 12
	moves = 8

	x = white
	o = black

	move_a = [x, x, o, x, x]
	move_b = [x, o, x, o, x]

	space = [o]*size

	dance_left  = [move_a+space, move_b+space]*moves
	dance_right = [space+move_a, space+move_b]*moves

	slide_right = [space[:i] + move_b + space[i:] for i, _ in enumerate(space)]
	slide_left  = [space[i:] + move_b + space[:i] for i, _ in enumerate(space)]

	return dance_left + slide_right + dance_right + slide_left

monster = [purple]*3 + [white] + [purple]*5 + [white] + [purple]*3
pumpkin_spice = [purple] + [orange]*4
spooky = [red, orange, green, purple]

def Halloween(count: int):
	return [
		Dance(count, skeleton_dance(), dancers=4),
		Scroll(count, spooky, 1),
		Scroll(count, spooky, -1),
		NightRider(count, monster),
		Scroll(count, pumpkin_spice, 1),
		Scroll(count, pumpkin_spice, -1),
		Growth(count),
	]