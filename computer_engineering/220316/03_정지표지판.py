# Exercise03_12.py
# -*- coding: utf-8 -*-

import turtle

turtle.pensize(3)
turtle.penup()
turtle.goto(0,0)
turtle.setheading(330)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(40, steps=6)
turtle.end_fill()
turtle.penup()
turtle.goto(-2,18)
turtle.color("white")
turtle.write("정지", font=("맑은 고딕", 18, "bold"))
turtle.hideturtle()
turtle.done()