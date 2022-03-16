# Exercise03_16.py
# -*- coding: utf-8 -*-
import turtle
turtle.pensize(3) # Set pen thickness to 3 pixels
turtle.penup() # Pull the pen up
turtle.goto(-200, -50)
turtle.setheading(60)
turtle.pendown() # Pull the pen down
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("red")
turtle.circle(40, steps = 3) # Draw a triangle
turtle.end_fill() # Fill the shape
turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("blue")
turtle.setheading(45)
turtle.circle(40, steps = 4) # Draw a square
turtle.end_fill() # Fill the shape
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("green")
turtle.setheading(35)
turtle.circle(40, steps = 5) # Draw a pentagon
turtle.end_fill() # Fill the shape
#-------------------------------------------------
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.begin_fill() # 도형 내부를 색상으로 채우기 시작한다.
turtle.color("yellow")
turtle.circle(40, steps = 6) # 육각형을 그린다.
turtle.end_fill() # 도형을 색상으로 채운다.
turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.begin_fill() # 도형 내부를 색상으로 채우기 시작한다.
turtle.color("purple")
turtle.circle(40) # 원을 그린다.
turtle.end_fill() # 도형을 색상으로 채운다.
turtle.color("red")
turtle.penup()
turtle.goto(-115, 50)
turtle.pendown()
turtle.write("화려한 색의 도형",
      font = ("맑은 고딕", 18, "bold"))
turtle.hideturtle()
turtle.done()