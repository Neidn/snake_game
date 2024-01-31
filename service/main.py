from turtle import Turtle, Screen
import time

size = dict(
    width=600,
    height=600,
    width_half=300,
    height_half=300,
)

is_game_on = True
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segement_list = []

screen = Screen()
screen.setup(width=size["width"], height=size["height"])
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

for position in starting_position:
    segement = Turtle("square")
    segement.color("white")
    segement.penup()
    segement.goto(position)
    segement_list.append(segement)
    screen.update()

while is_game_on:
    screen.update()
    time.sleep(0.2)

    # Move segement
    # segement_list[0].forward(20)
    # segement_list[1].goto(segement_list[0].position())
    # segement_list[2].goto(segement_list[1].position())

    for segement in range(len(segement_list) - 1, 0, -1):
        new_x = segement_list[segement - 1].xcor()
        new_y = segement_list[segement - 1].ycor()
        segement_list[segement].goto(new_x, new_y)

    segement_list[0].forward(20)



screen.exitonclick()
