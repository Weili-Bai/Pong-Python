from turtle import Turtle

FONT = ('Courier', 30, 'normal')


class ScoreBoard(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(pos)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=FONT)
