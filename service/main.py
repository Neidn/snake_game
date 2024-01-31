from turtle import Turtle, Screen

size = {
    "width": 600,
    "height": 600,
}

starting_position = [(0, 0), (-20, 0), (-40, 0)]

segement_list = []

screen = Screen()
screen.setup(width=size["width"], height=size["height"])
screen.bgcolor("black")
screen.title("Snake Game")

for position in starting_position:
    segement = Turtle("square")
    segement.color("white")
    segement.goto(position)
    segement_list.append(segement)

screen.exitonclick()
