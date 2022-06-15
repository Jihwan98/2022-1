import turtle
import random

swidth, sheight = 500, 500
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth, sheight)

shape = turtle.getshapes()

for _ in range(10):
    random.shuffle(shape)
    myTurtle = turtle.Turtle(shape[0])
    tX, tY = random.randint(-swidth/2, swidth/2), random.randint(-sheight/2, sheight/2)
    rgb = (random.random(), random.random(), random.random())
    tSize = random.randint(1, 5)
    myTurtle.color(rgb)
    myTurtle.turtlesize(tSize)
    myTurtle.goto(tX, tY)

turtle.hideturtle()
turtle.done()