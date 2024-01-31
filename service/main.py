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
    for segement in segement_list:
        segement.forward(20)

    segement_list[0].left(90)

screen.exitonclick()
