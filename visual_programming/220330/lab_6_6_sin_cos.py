# python_graph_01.py
import turtle
import math
t = turtle.Turtle()
t.shape("turtle")
t.goto(400, 0)
t.goto(0, 0)
t.goto(0, 200)
t.goto(0, 0)
t.color("red")
t.speed(0) # 속도가 빠르다.
t.hideturtle()
for x in range(0, 360, 3) :
    t.goto(x, 100*math.sin(x*3.14/180))
t.write("sin")

t.penup()
t.goto(0, 100)
t.pendown()
t.color("blue")
for x in range(0, 360, 3) :
    t.goto(x, 100*math.cos(x*3.14/180))
t.write("cos")

t.hideturtle() # add line 

turtle.done()
