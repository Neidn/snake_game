from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.create_snake()

    def create_snake(self):
        self.segement_list = []

        for position in STARTING_POSITIONS:
            segement = Turtle("square")
            segement.color("white")
            segement.penup()
            segement.goto(position)
            self.segement_list.append(segement)

        self.head = self.segement_list[0]

    # Move segement
    # segement_list[0].forward(20)
    # segement_list[1].goto(segement_list[0].position())
    # segement_list[2].goto(segement_list[1].position())
    def move(self):
        for segement in range(len(self.segement_list) - 1, 0, -1):
            new_x = self.segement_list[segement - 1].xcor()
            new_y = self.segement_list[segement - 1].ycor()
            self.segement_list[segement].goto(new_x, new_y)

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
