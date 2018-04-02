import turtle
import math
DIST = 1
while DIST < 400:
	turtle.forward(DIST)
	turtle.right(65)
	turtle.forward(DIST)
	turtle.right(70)
	turtle.right(65)
	DIST = math.sqrt(DIST*DIST+DIST*DIST)
	turtle.forward(DIST)
	turtle.left(65)
	turtle.forward(DIST)
	turtle.left(70)
	turtle.forward(DIST)
