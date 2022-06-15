import turtle
import random

swidth, sheight = 500, 500

turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth, sheight)

shapeList = turtle.getshapes()

for i in range(10):
    random.shuffle(shapeList)
    myturtle = turtle.Turtle(shapeList[0])
    rgb = (random.random(), random.random(), random.random())
    tSize = random.randrange(1, 4)
    tX, tY = random.randint(-swidth/2, swidth/2), random.randint(-sheight/2, sheight/2)

    myturtle.color(rgb)
    myturtle.turtlesize(tSize)
    myturtle.goto(tX, tY)

turtle.done()