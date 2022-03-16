import turtle
import random

swidth, sheight, tSize, pSize, tAngle, count, tcolor = 300, 300, 0, 0, 0, 0, 0
r, g, b = 0.0, 0.0, 0.0
colors = ["red", "purple", "blue", "green", "yellow", "orange"]

turtle.setup(width=swidth+30, height=sheight+30)
turtle.screensize(swidth, sheight)

def screenLeftClick(x, y):
    global r, g, b, count
    count += 1
    tSize = random.randrange(1, 4)
    turtle.shapesize(tSize)

    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color(r, g, b)
    
    tAngle = random.randrange(0,360)
    turtle.pendown()
    turtle.goto(x,y)
    turtle.left(tAngle)
    pSize = random.randrange(1,5)
    turtle.pensize(pSize)
    tcolor = random.randrange(0,6)
    turtle.fillcolor(colors[tcolor])
    turtle.stamp()
    print("count=%2d, shape_size=%2d, pen_size=%2s, pen_color=%7s,\
 x=%4d, y=%4d" % (count, tSize, pSize, colors[tcolor], x, y))


turtle.title('거북이 도장 찍기')
turtle.shape('turtle')

turtle.onscreenclick(screenLeftClick, 1)

turtle.done()