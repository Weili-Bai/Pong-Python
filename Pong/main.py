from turtle import Screen
import time
from Player import Player
from Ball import Ball
from ScoreBoard import ScoreBoard
import Other


WINDOW_WIDTH=1080
WINDOW_HEIGHT=720
window=Screen()
window.setup(WINDOW_WIDTH,WINDOW_HEIGHT)
window.bgcolor("black")
window.title("Pong")
p0_size=Other.get_size(window)
p1_size=Other.get_size(window)
window.tracer(0)
window.listen()
p0=Player(p0_size,0)
p1=Player(p1_size,1)
rackets=p0.racket+p1.racket
ball=Ball()
window.onkeypress(fun=p0.up,key='w')
window.onkeypress(fun=p0.down,key='s')
window.onkeypress(fun=p1.up,key='Up')
window.onkeypress(fun=p1.down,key='Down')
ball.new_round(0)
window.onkey(fun=lambda: ball.start_round(0), key='d')
window.onkey(fun=lambda: ball.start_round(1), key='Left')
s0=ScoreBoard((-40,300))
s1=ScoreBoard((40,300))
line=Other.get_line(window)
while Other.is_game_on(s0.score,s1.score):
    window.update()
    time.sleep(0.1)
    ball.move(rackets)
    if ball.is_round_over():
        x=ball.ball.xcor()
        if x>0:
            s0.score+=1
            s0.write_score()
            ball.new_round(0)
        else:
            s1.score+=1
            s1.write_score()
            ball.new_round(1)
if s0.score==Other.WINNING_SCORE:
    winner=1
else:
    winner=2
window.clear()
window.bgcolor("black")
result=Other.get_result(winner)
window.exitonclick()
