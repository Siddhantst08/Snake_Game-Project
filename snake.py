from turtle import Turtle

STARTING_TUPLE = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtle_list = []
        self.create_turtle()
        self.head = self.turtle_list[0]

    def create_turtle(self):
        for pos in STARTING_TUPLE:
            self.add_segments(pos)

    def add_segments(self, pos):
        my_turtle = Turtle("square")
        my_turtle.color("white")
        my_turtle.penup()
        my_turtle.goto(pos)
        self.turtle_list.append(my_turtle)

    def extend(self):
        self.add_segments(self.turtle_list[-1].position())

    def move(self):
        for turtle_num in range(len(self.turtle_list) - 1, 0, -1):
            x = self.turtle_list[turtle_num - 1].xcor()
            y = self.turtle_list[turtle_num - 1].ycor()
            self.turtle_list[turtle_num].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


