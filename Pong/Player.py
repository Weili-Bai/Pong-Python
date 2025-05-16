from turtle import Turtle
STEP=20
class Player:
    def __init__(self,size,player):
        self.racket = []
        y=size / 2 * STEP
        if player == 0:
            colour="red"
            x = -520
        else:
            colour="yellow"
            x=510
        for _ in range(0, size):
            self.create_segments((x, y), colour)
            y -= STEP
        self.size=size
        self.head=self.racket[0]
        self.tail=self.racket[size-1]
        self.head.setheading(90)
        self.tail.setheading(270)

    def create_segments(self,position,colour):
        curr=Turtle()
        curr.shape("square")
        curr.color(colour)
        curr.penup()
        curr.goto(position)
        curr.shapesize(1,0.25)
        self.racket.append(curr)

    def up(self):
        if self.head.ycor()>=340:
            return
        for i in range (self.size-1, 0,-1):
            x = self.racket[i-1].xcor()
            y = self.racket[i-1].ycor()
            self.racket[i].goto(x,y)
        self.head.forward(STEP)

    def down(self):
        if self.tail.ycor()<-320:
            return
        size=len(self.racket)
        for i in range (0, size-1):
            x = self.racket[i+1].xcor()
            y = self.racket[i+1].ycor()
            self.racket[i].goto(x,y)
        self.tail.forward(STEP)
