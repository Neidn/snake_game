from turtle import Turtle, Screen

size = {
    "width": 600,
    "height": 600,
}

screen = Screen()
screen.setup(width=size["width"], height=size["height"])
screen.bgcolor("black")
screen.title("Snake Game")

screen.exitonclick()
