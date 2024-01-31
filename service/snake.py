from turtle import Turtle

from config import *

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segment_list = []
        self.create_snake()

    def create_snake(self):
        self.segment_list = []

        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segment_list.append(segment)

        self.head = self.segment_list[0]

    # Move segment
    # segment_list[0].forward(20)
    # segment_list[1].goto(segment_list[0].position())
    # segment_list[2].goto(segment_list[1].position())
    def move(self):
        for segment in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[segment - 1].xcor()
            new_y = self.segment_list[segment - 1].ycor()
            self.segment_list[segment].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
