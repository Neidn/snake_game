from turtle import Screen
import time

from service.snake import Snake
from service.config import *
from service.food import Food
from service.scoreboard import ScoreBoard

is_game_on = True

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Listen to keystrokes
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
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > WIDTH_HALF - 20 or snake.head.xcor() < -WIDTH_HALF + 20 or snake.head.ycor() > HEIGHT_HALF - 20 or snake.head.ycor() < -HEIGHT_HALF + 20:
        is_game_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segment_list[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
