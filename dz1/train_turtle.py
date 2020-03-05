from turtle import *
from random import *


def randrange_without_zero(left, right):
    res = randrange(left, right)
    while res == 0:
        res = randrange(left, right)
    return res


def check_if_end_of_canvas(rad, ang):
    position = pos()
    if abs(position[0]) > window_width() // 2 or abs(position[1]) > window_height() // 2:
        circle(rad, -ang)  # going right back


# TODO: do not go off screen -- done with check_if_end_of_canvas
# TODO: eliminate small radius -- done with randrange_without_zero
pensize(3)
for i in range(100):
    print(pos())
    color(random(), random(), random())
    radius, angle = randrange_without_zero(-60, 60), randrange(10, 200)
    circle(radius, angle)
    check_if_end_of_canvas(radius, angle)

exitonclick()
