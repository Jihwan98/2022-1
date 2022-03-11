import turtle
import random

def screenRightClick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    turtle.pensize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color(r, g, b)
    turtle.pendown()
    turtle.goto(x,y)
    turtle.stamp()


pSize, tSize = 10, 0
r, g, b = 0.0, 0.0, 0.0

turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenRightClick, 3)

turtle.done()