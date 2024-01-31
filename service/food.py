from turtle import Turtle
import random

from service.config import *


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

        self.refresh()

    def refresh(self):
        random_x = random.randint(-WIDTH_HALF + 20, WIDTH_HALF - 20)
        random_y = random.randint(-HEIGHT_HALF + 20, HEIGHT_HALF - 20)

        self.goto(random_x, random_y)
