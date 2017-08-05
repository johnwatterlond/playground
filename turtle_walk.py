"""
Module used to simulate random walks with turtle geometry.


This module was created while reading parts of `Turtle Geometry` by
Harold Abelson and Andrea diSessa.


Examples:
    t = TurtleWalk()
    t.speed(0)
    ts = t.turtle.screen
    ts.delay(0)

    t.random_walk_in_shape((5,5), (-30, 30), 1000, Circle, 150)
    t.random_walk_in_shape((5,5), (-30, 30), 1000, Box, 150)

    turtle.mainloop()
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


class Shape():
    """
    Represents a shape.

    Args:
        size: the size of the shape.

    Attributes:
        size: the size of the shape.
    """
    def draw(self, t, size):
        """
        Draw Shape with turtle t of size size.
        """

    def contains(self, point):
        """
        Return True if Shape contains Point point.
        """

    def contains_move(self, t, distance):
        """
        Return true if turtle t is in shape after moving forward by
        distance distance.
        """
        current_position = t.pos()
        t.silent_forward(distance)
        proposed_position = t.pos()
        t.go_to(current_position)
        return self.contains(proposed_position)


class Box(Shape):
    """
    Represents a box.  A box is a square centered at (0, 0) with
    side lengths box.size * 2.
    """
    def __init__(self, size):
        self.size = size

    def draw(self, t):
        t.go_to(Point(-self.size, -self.size))
        for i in range(4):
            t.forward(self.size * 2)
            t.left(90)
        t.go_home()

    def contains(self, point):
        return abs(point.x) < self.size and abs(point.y) < self.size


class Circle(Shape):
    def __init__(self, size):
        self.size = size

    def draw(self, t):
        t.go_to(Point(0, -self.size))
        t.circle(self.size)
        t.go_home()

    def contains(self, point):
        return point.distance(Point(0,0)) < self.size


class TurtleWalk(turtle.Turtle):
    """
    Represents a turtle for random walks.

    Inherits attributes and methods from turtle.Turtle. Note that
    turtle.pos() is redefined.

    Args:
        home: Turtle's home as Point(x, y). Default is origin.

    Attributes:
        home: Turtle's home as Point(x, y).
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

    def wriggle(self):
        """
        Turtle turns at a random angle.
        """
        t.right(random.randint(-180, 180))

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

    def random_walk_in_shape(self, step_size, turn_angle, num_steps, Shape, shape_size):
        """
        Turtle goes for a random walk inside a Shape shape of size
        size for num_steps steps.
        If a step causes turtle to leave shape, instead of taking
        that step turtle turns at a random angle and then tries to
        take the step.  Turtle does this until it can take the step.

        step_size = (min_step_size, max_step_size)
        turn_angle = (min_turn_angle, max_turn_angle)

        Each step has a random angle theta and random step length
        dist such that:
        min_turn_angle <= theta <= max_turn_angle
        and
        min_step_size <= dist <= max_step_size
        """
        shape = Shape(shape_size)
        shape.draw(self)
        step = 0
        while step < num_steps:
            self.left(random.uniform(*turn_angle))
            distance = random.uniform(*step_size)
            if shape.contains_move(self, distance):
                self.forward(distance)
            else:
                while not shape.contains_move(self, distance):
                    self.wriggle()
                self.forward(distance)
            step = step + 1










def main():
    t = TurtleWalk()
    t.speed(0)
    ts = t.turtle.screen
    ts.delay(0)

    t.random_walk_in_shape((5,5), (-30, 30), 1000, Circle, 150)
    t.random_walk_in_shape((5,5), (-30, 30), 1000, Box, 150)

    turtle.mainloop()

if __name__ == '__main__':
    main()
