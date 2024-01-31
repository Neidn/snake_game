from turtle import Screen
from snake import Snake
import time

size = dict(
    width=600,
    height=600,
    width_half=300,
    height_half=300,
)

is_game_on = True

snake = Snake()

screen = Screen()
screen.setup(width=size["width"], height=size["height"])
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Listen to key strokes
screen.listen()

# Move snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "Down")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "Right")
screen.onkey(snake.right, "d")

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
