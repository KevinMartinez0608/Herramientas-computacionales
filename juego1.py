from turtle import *
import turtle
import math
from freegames import vector

"speed to mke the figures"
speed(0)

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end): # make a circle
    "Draw circle from start to end."
    pi = 3.141592
    diametro = end.x - start.x
    radio = diametro / 2
    circunferencia = 2 * pi * radio
    arco = circunferencia / 360

    # TODO
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for i in range(360):
        forward(arco)
        right(1)

    end_fill()



def rectangle(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        if count % 2 == 0:
            forward((end.x - start.x) * 2)
            left(90)
        else:
            forward(end.x - start.x)
            left(90)

    end_fill()


def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)

    end_fill()


def tap(x, y):
    "Store starting point or draw shape."
    start = state["start"]

    if start is None:
        state["start"] = vector(x, y)
    else:
        shape = state["shape"]
        end = vector(x, y)
        shape(start, end)
        state["start"] = None


def store(key, value):
    "Store value in state at key."
    state[key] = value


state = {"start": None, "shape": line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, "u")
onkey(lambda: color("black"), "K")
onkey(lambda: color("white"), "W")
onkey(lambda: color("green"), "G")
onkey(lambda: color("blue"), "B")
onkey(lambda: color("red"), "R")
onkey(lambda: color("orange"), "O")
onkey(lambda: store("shape", line), "l")
onkey(lambda: store("shape", square), "s")
onkey(lambda: store("shape", circle), "c")
onkey(lambda: store("shape", rectangle), "r")
onkey(lambda: store("shape", triangle), "t")
done()
