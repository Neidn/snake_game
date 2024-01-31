from turtle import Screen
import time

from snake import Snake
from config import *
from food import Food
from scoreboard import ScoreBoard

is_game_on = True

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Listen to key strokes
screen.listen()

# Move snake
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_down, "s")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_right, "d")

while is_game_on:
    screen.update()
    time.sleep(0.05)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < (MOVE_DISTANCE - 5):
        food.refresh()
        scoreboard.increase_score()
        # snake.extend()

    # detect collision with wall
    if snake.head.xcor() > WIDTH_HALF or snake.head.xcor() < -WIDTH_HALF or snake.head.ycor() > HEIGHT_HALF or snake.head.ycor() < -HEIGHT_HALF:
        is_game_on = False
        scoreboard.game_over()

screen.exitonclick()
