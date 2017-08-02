"""
Module used to simulate random walks with turtle geometry.


This module was created while reading parts of `Turtle Geometry` by
Harold Abelson and Andrea diSessa.


Make sure to set the turtle speed to zero and the screen delay to
zero.
"""

import turtle
import math
import random


class Point:
    """
    Represents a point in 2-dimensions.

    Args:
        x: x-coordinate of point.
        y: y-coordinate of point.

    Attributes:
        x: x-coordinate of point.
        y: y-coordinate of point.

    methods:
        distance(other): Distance to Point other.
        is_in_box(boxsize): Is point in box of size boxsize.
        is_in_circle(radius): Is point in circle of radius radius.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        """
        Calculate the distance between self and Point other.
        """
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt((dx)**2 + (dy)**2)

    def is_in_box(self, boxsize):
        """
        Check if point is in box of size boxsize.
        """
        return abs(self.x) < boxsize and abs(self.y) < boxsize

    def is_in_circle(self, radius):
        """
        Check if point is in circle of radius radius.

        In this context, a circle is a circle centered at (0, 0).
        """
        return self.distance(Point(0,0)) < radius


class TurtleWalk(turtle.Turtle):
    """
    Represents a turtle for random walks.

    Inherits attributes and methods from turtle.Turtle. Note that
    turtle.pos() is redefined.

    Args:
        home: Turtle's home as Point(x, y). Default is origin.

    Attributes:
        home: Turtle's home as Point(x, y).

    methods:
        pos():
        is_home(epsilon=.001):
        go_to(point):
        go_home():
        silent_forward(distance):
        draw_polygon(side_length, num_sides):
        draw_square(side_length, num_sides):
        draw_box(boxsize):
        is_move_in_box(distance, boxsize):
        random_walk(step_size, turn_angle, num_steps):
        random_walk_in_box(step_size, turn_angle, num_steps, boxsize):
        draw_circle(radius):
        is_move_in_circle(distance, radius):
        random_walk_in_circle(self, step_size, turn_angle, num_steps, radius):
    """
    def __init__(self, home=Point(0, 0)):
        self.home = home
        super().__init__()

    def pos(self):
        """
        Return position of turtle as a Point.
        """
        return Point(*self.position())

    def is_home(self, epsilon=.001):
        """
        Check if turtle is within epsilon its home.
        """
        return self.pos().distance(self.home) < epsilon

    def go_to(self, point):
        """
        Move turtle to coordinates of Point point without drawing
        any lines.
        """
        self.hideturtle()
        self.penup()
        self.setposition(point.x, point.y)
        self.pendown()
        self.showturtle()

    def go_home(self):
        """
        Return turtle back home without drawing lines.
        """
        self.go_to(Point(0, 0))

    def silent_forward(self, distance):
        """
        Hide turtle and move forward by distance without drawing
        any lines.

        This method is meant to be followed by go_to() and as such
        leaves turtle hidden and pen up.
        """
        self.hideturtle()
        self.penup()
        self.forward(distance)

    def draw_polygon(self, side_length, num_sides):
        """
        Turtle draws a regular polygon with side lengths
        side_length.
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
        Turtle draws a box of size boxsize.

        A box is defined as a square centered at (0, 0).
        The size of a box is defined as the (shortest) distance
        from the center of the box to any of its sides.
        """
        self.go_to(Point(-boxsize, -boxsize))
        self.draw_square(boxsize * 2)
        self.go_home()

    def is_move_in_box(self, distance, boxsize):
        """
        Return True if by going forward by distance, turtle is in
        the box of size boxsize.
        """
        current_position = self.pos()
        self.silent_forward(distance)
        proposed_position = self.pos()
        self.go_to(current_position)
        return proposed_position.is_in_box(boxsize)

    def random_walk(self, step_size, turn_angle, num_steps):
        """
        Turtle goes for a random walk for num_steps steps.

        step_size = (min_step_size, max_step_size)
        turn_angle = (min_turn_angle, max_turn_angle)

        Each step has a random angle theta and random step length
        dist such that:
        min_turn_angle <= theta <= max_turn_angle
        and
        min_step_size <= dist <= max_step_size
        """
        step = 0
        while step < num_steps:
            self.left(random.uniform(*turn_angle))
            self.forward(random.uniform(*step_size))
            step = step + 1

    def random_walk_in_box(self, step_size, turn_angle, num_steps, boxsize):
        """
        Turtle goes for a random walk inside a box of size boxsize
        for num_steps steps.
        If a step causes turtle to leave box, instead of taking
        that step turtle turns around.

        step_size = (min_step_size, max_step_size)
        turn_angle = (min_turn_angle, max_turn_angle)

        Each step has a random angle theta and random step length
        dist such that:
        min_turn_angle <= theta <= max_turn_angle
        and
        min_step_size <= dist <= max_step_size
        """
        self.draw_box(boxsize)
        step = 0
        while step < num_steps:
            self.left(random.uniform(*turn_angle))
            distance = random.uniform(*step_size)
            if self.is_move_in_box(distance, boxsize):
                self.forward(distance)
            else:
                self.left(180)
            step = step + 1

    def draw_circle(self, radius):
        """
        Turtle draws a circle of radius radius with center (0, 0).

        Returns home after circle is drawn.
        """
        self.go_to(Point(0, -radius))
        self.circle(radius)
        self.go_home()

    def is_move_in_circle(self, distance, radius):
        """
        Return True if by going forward by distance, turtle is in
        the circle centered at (0, 0) of radius radius.
        """
        current_position = self.pos()
        self.silent_forward(distance)
        proposed_position = self.pos()
        self.go_to(current_position)
        return proposed_position.is_in_circle(radius)

    def random_walk_in_circle(self, step_size, turn_angle, num_steps, radius):
        """
        Turtle goes for a random walk inside a circle of radius
        radius for num_steps steps.
        If a step causes turtle to leave circle, instead of taking
        that step turtle turns around.

        step_size = (min_step_size, max_step_size)
        turn_angle = (min_turn_angle, max_turn_angle)

        Each step has a random angle theta and random step length
        dist such that:
        min_turn_angle <= theta <= max_turn_angle
        and
        min_step_size <= dist <= max_step_size
        """
        self.draw_circle(radius)
        step = 0
        while step < num_steps:
            self.left(random.uniform(*turn_angle))
            distance = random.uniform(*step_size)
            if self.is_move_in_circle(distance, radius):
                self.forward(distance)
            else:
                self.left(180)
            step = step + 1


# TODO:
# instead of turning around, turtle should wriggle around.
# until it can do the move it wants?
# should a wriggle be counted in a single step. i.e. wriggle
# until step possible then make step, then continue on to next
# step?
def wriggle(t, distance, boxsize):
    out_of_bounds = True
    while out_of_bounds == True:
        t.right(distance)
        check_forward_and_move(t, distance, boxsize)



# TODO:
# instead of picking an angle from an interval,
# pick angle from a list.
def random_movesq_boxed(t, d, angle_list, steps, boxsize):
    i = 0
    draw_box(t, boxsize)
    while i < steps:
        t.lt(random.choice(angle_list))
        check_forward_and_move(t, random.uniform(d[0],d[1]), boxsize)
        i = i + 1




def main():
    t = TurtleWalk()
    ts = t.turtle.screen
    ts.delay(0)
    t.random_walk_in_box((5, 5), (-30, 30), 1000, 150)
    turtle.mainloop()

if __name__ == '__main__':
    main()
