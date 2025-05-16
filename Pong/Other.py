from turtle import Turtle

FONT = ('Courier', 30, 'normal')


def get_size(window):
    result = window.numinput(title="Size", prompt="What size of value do you want?", minval=3, maxval=8)
    return int(result)


def get_line(window):
    size = int(window.window_height() / 20)
    result = []
    y = window.window_width() / 2
    for _ in range(0, size * 2):
        curr = Turtle()
        curr.shape("square")
        curr.penup()
        curr.color("green")
        curr.goto(0, y)
        y -= 20
        curr.shapesize(0.5, 0.25)
        result.append(curr)
    return result


def is_game_on(num1, num2):
    return num1 < 11 and num2 < 11


def get_result(num):
    result = Turtle()
    result.color("white")
    result.penup()
    result.hideturtle()
    result.write(f"Player{num} is the winner!", align='center', font=FONT)
    return result
