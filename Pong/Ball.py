from turtle import Turtle
import random
from Player import STEP

LEFT = 180
RIGHT = 0


class Ball:
    def __init__(self):
        self.is_moving = False
        self.ball = Turtle()
        self.ball.penup()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.shapesize(0.75)
        self.new_round(0)

    def new_round(self, side):
        self.is_moving = False
        if side == 0:
            self.ball.goto(-40, 0)
        else:
            self.ball.goto(40, 0)

    def start_round(self, side):
        if self.is_moving:
            return
        self.is_moving = True
        angel1 = random.randint(23, 60)
        sign = random.randint(0, 1)
        if sign:
            angel = angel1
        else:
            angel = angel1 * -1
        if side == 0:
            self.ball.setheading(RIGHT + angel)
        else:
            self.ball.setheading(LEFT + angel)

    def move(self, racket):
        if self.is_moving:
            if self.is_hit_wall():
                self.ball.setheading(360 - self.ball.heading())
            if self.is_hit_player(racket):
                self.ball.setheading(180 - self.ball.heading())
                self.ball.setheading(self.ball.heading() % 360)
            self.ball.forward(STEP * 1.5)

    def is_hit_wall(self):
        y = self.ball.ycor()
        return y >= 340 or y <= -330

    def is_hit_player(self, racket):
        for pos in racket:
            if self.ball.distance(pos) < 15:
                return True
        return False

    def is_round_over(self):
        x = self.ball.xcor()
        return x < -660 or x > 660
