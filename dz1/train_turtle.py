from turtle import *
from random import *

# TODO: do not go off screen
# TODO: eliminate small radius

pensize(3)

for i in range(100):
    color(random(), random(), random())
    circle(randrange(-60,60), randrange(10,200))

exitonclick()