from turtle import Screen, Turtle
from Paddle import Paddle
from Ball import Ball
import time
from ScoreBoard import ScoreBoard

window = Screen()
window.bgcolor("black")
window.setup(width=800, height=600)
window.title("Pong")
window.tracer(0)

lp = Paddle((-350, 0))
rp = Paddle((350, 0))
ball = Ball()
score_board = ScoreBoard()

window.listen()
window.onkey(rp.go_up, "Up")
window.onkey(rp.go_down, "Down")
window.onkey(lp.go_up, "w")
window.onkey(lp.go_down, "s")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    window.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(rp) < 50 and ball.xcor() > 320 or ball.distance(lp) < 50 and ball.xcor() < -320:
        ball.hit_paddle()
    if ball.xcor() > 380:
        ball.reset()
        score_board.lplus()

    if ball.xcor() < -380:
        ball.reset()
        score_board.rplus()
window.exitonclick()
