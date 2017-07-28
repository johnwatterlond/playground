import turtle
import math
import random


bob = turtle.Turtle()
ts = turtle.getscreen()
ts.clear()


ts.screensize(5000,5000)
bob.speed(0)
ts.delay(0)



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        """
        Calculate the distance between self and point other.
        """
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt((dx)**2 + (dy)**2)


class my_turtle(turtle.Turtle):
    def __init__(self, home=Point(0, 0)):
        self.home = home
        super().__init__()

    def pos(self):
        return Point(*self.position())

    def is_home(self, epsilon=.001):
        """
        Check if turtle is within epsilon its home.
        """
        return self.pos().distance(self.home) < epsilon

    def goto(self, x, y):
        """
        Move turtle to coordinates (x, y) without drawing any lines.
        """
        self.penup()
        self.setposition(x, y)
        self.pendown()

    def go_home(self):
        """
        Return turtle back home without drawing lines.

        home is defined as (0, 0).
        """
        self.goto(0, 0)

    def draw_polygon(self, side_length, num_sides):
        """
        Turtle draws a regular polygon with side lengths side_length.
        """
        for i in range(num_sides):
            self.forward(side_length)
            self.left(360 / num_sides)

    def draw_square(self, side_length):
        """
        Turtle draws a square with side lengths side_length.
        """
        self.draw_polygon(side_length, 4)

    def draw_box(self, boxsize):
        """
        Turtle draws box centered at (0,0) with side length
        boxsize * 2 and then return home.
        """
        self.goto(-boxsize, -boxsize)
        self.draw_square(boxsize * 2)
        self.go_home()


def random_move(t, d=(10, 10), a=(-180, 180), num_steps=1000):
    """
    d = (min_dist, max_dist)
    a = (min_angle, max_angle)
    """
    i = 0
    while i < num_steps:
        t.lt(random.uniform(a[0], a[1]))
        t.fd(random.uniform(d[0], d[1]))
        i = i + 1

#random_move(bob, (3, 10), (-180, 180), 5000)




# TODO:
# want to make these two functions better...
# get wriggle working, think it is not working because
# check_forward_and_move does two things! so fix that. so for
# example, instead of wriggling the turtle turns around.


def check_forward_and_move(t, distance, boxsize):
    """
    If moving turtle t forward by distance distance keeps
    t in the box, moves t forward by distance.  Else turns around.
    """
    old_pos = t.pos()

    t.penup()
    t.hideturtle()
    t.forward(distance)

    out_of_bounds = check_out_of_bounds(t, boxsize)

    t.goto(old_pos)
    t.pendown()
    t.showturtle()

    if out_of_bounds == False:
        t.forward(distance)
    else:
        t.right(180)


def check_out_of_bounds(t, boxsize):
    if abs(t.xcor()) > boxsize or abs(t.ycor()) > boxsize:
        return True
    else:
        return False


def random_move_boxed(t, d, a, steps, boxsize):
    i = 0
    draw_box(t, boxsize)
    while i < steps:
        t.lt(random.uniform(a[0], a[1]))
        check_forward_and_move(t, random.uniform(d[0],d[1]), boxsize)
        i = i + 1


#TODO: fix this wriggle shit.
def wriggle(t, distance, boxsize):
    out_of_bounds = True
    while out_of_bounds == True:
        t.right(distance)
        check_forward_and_move(t, distance, boxsize)


def draw_box(t, boxsize):
    """
    Draw box centered at (0,0) with side length
    boxsize*2.
    Returns t=turtle back home afterwards.
    """
    t.penup()
    t.goto(-boxsize,-boxsize)
    t.pendown()
    draw_square(t, boxsize * 2)
    return_home(t)



#random_move_boxed(bob, (4, 4), (-180, 180), 5000, 150)
#random_move_boxed(bob, (4, 4), (-10, 10), 5000, 150)
#random_move_boxed(bob, (4, 4), (-45, 45), 5000, 150)




def random_movesq_boxed(t, d, a, steps, boxsize):
    i = 0
    draw_box(t, boxsize)
    while i < steps:
        t.lt(random.choice(a))
        check_forward_and_move(t, random.uniform(d[0],d[1]), boxsize)
        i = i + 1
