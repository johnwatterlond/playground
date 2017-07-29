import turtle
import math
import random


t = turtle.Turtle()
ts = turtle.getscreen()
ts.clear()


ts.screensize(5000,5000)
t.speed(0)
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

    def is_in_box(self, boxsize):
        """
        Check if point is in box with side length boxsize.
        """
        return abs(self.x) < boxsize and abs(self.y) < boxsize


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
        self.hideturtle()
        self.penup()
        self.setposition(x, y)
        self.pendown()
        self.showturtle()

    def go_home(self):
        """
        Return turtle back home without drawing lines.

        home is defined as (0, 0).
        """
        self.goto(0, 0)

    def silent_forward(self, distance):
        """
        Hide turtle and move forward by distance without drawing
        any lines.

        This method is meant to be followed by goto() and as such
        leaves turtle hidden and pen up.
        """
        self.hideturtle()
        self.penup()
        self.forward(distance)

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

    def is_move_in_box(self, distance, boxsize):
        """
        Return True if going forward by distance will keep turtle
        in box with side length boxsize.
        """
        current_position = self.position()
        self.silent_forward(distance)
        proposed_position = Point(*self.position())
        self.goto(*current_position)
        return proposed_position.is_in_box(boxsize)

    def random_walk(self, step_size, angle, num_steps):
        """
        Turtle goes for a random walk for num_steps steps.

        step_size = (min_step_size, max_step_size)
        angle = (min_angle, max_angle)

        Each step has a random angle theta and random step length dist
        such that:
        min_angle <= theta <= max_angle
        and
        min_step_size <= dist <= max_step_size
        """
        step = 0
        while step < num_steps:
            self.left(random.uniform(*angle))
            self.forward(random.uniform(*step_size))
            step = step + 1



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
