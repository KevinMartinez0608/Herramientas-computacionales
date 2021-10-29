from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(-190, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
count=0
c=['blue','orange','dark green','brown','purple']


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def colorRandom(c):
    #Change the color randomly
    color=random.choice(c)
    c.remove(color)
    return color 

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

#move food

def foodRandomly():
    global count
    if count == 30:
        if random.choice([True, False]):
            if food.y == 100:
                food.y = food.y - 10
            elif food.y == -100:
                food.y = food.y + 10
            else:
                if random.choice([True, False]):
                    food.y = food.y - 10
                else:
                    food.y = food.y + 10
            count = 0
        else:
            if food.x == 100:
                food.x = food.x - 10
            elif food.x == -100:
                food.x = food.x + 10
            else:
                if random.choice([True, False]):
                    food.x = food.x - 10
                else:
                    food.x = food.x + 10
            count = 0
            


def move():
    "Move snake forward one segment."
    global count
    count+=15
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9,snakeColor)
    foodRandomly()
    square(food.x, food.y, 9,foodColor)
    update()
    ontimer(move, 100)


snakeColor=colorRandom(c)
foodColor=colorRandom(c)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
