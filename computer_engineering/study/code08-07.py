import turtle
import random
from tkinter.simpledialog import *

from matplotlib import widgets

swidth, sheight = 500, 500
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth, sheight)
turtle.penup()

inChr = askstring('문자열 입력', '거북이 쓸 문자열 입력')

for ch in inChr:
    rgb = (random.random(), random.random(), random.random())
    tX, tY = random.randint(-swidth/2, swidth/2), random.randint(-sheight/2, sheight/2)
    txtSize = random.randrange(1, 30)
           
    turtle.goto(tX, tY)
    turtle.pencolor(rgb)
    turtle.write(ch, font=('맑은고딕', txtSize, 'bold'))

turtle.done()