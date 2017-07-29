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



#TODO:
# make my turtle class work better with Point class.
# when calling like t.pos() it returns a Point object.
# I should also be able to do something like t.goto(Point)
# i.e. pass a Point object to t.goto().

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
        self.goto(-boxsize, -boxsize)
        self.draw_square(boxsize * 2)
        self.go_home()

    def is_move_in_box(self, distance, boxsize):
        """
        Return True if by going forward by distance, turtle is in
        the box of size boxsize.
        """

        # TODO:
        # current_position is a tuple while proposed_position is
        # a Point().  This could be confusing when reading later.
        # Fix this issue.
        current_position = self.position()
        self.silent_forward(distance)
        proposed_position = Point(*self.position())
        self.goto(*current_position)
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
        self.goto(0, -radius)
        self.circle(radius)
        self.go_home()

    def is_move_in_circle(self, distance, radius):
        """
        Return True if by going forward by distance, turtle is in
        the circle of radius radius.
        """

        # TODO:
        # DRY. this is basically verbatim copy of
        # is_move_in_box.
        current_position = self.position()
        self.silent_forward(distance)
        proposed_position = Point(*self.position())
        self.goto(*current_position)
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
# make names for box and draw_box similar to circle/draw_circle...
def draw_circle(t, radius):
    t.goto(0, -radius)
    t.circle(radius)
    t.go_home()







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
