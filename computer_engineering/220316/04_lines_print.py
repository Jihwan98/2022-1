# Exercise01_17_black_red_blue.py
import turtle
turtle.penup()
turtle.goto(-39, 48) 
turtle.pendown()
turtle.write("(-39, 48)")
turtle.goto(50, -50) 
turtle.write("(50, -50)")
turtle.penup()
turtle.goto(-39+80, 48) 
turtle.pendown()
turtle.color("red") 
turtle.write("(-39+80, 48)")
turtle.goto(50+80, -50) 
turtle.write("(50+70, -50)")
turtle.penup()
turtle.goto(-39+80+80, 48) 
turtle.pendown()
turtle.color("blue") 
turtle.write("(-39+80+80, 48)")
turtle.goto(50+80+80, -50) 
turtle.write("(50+80+80, -50)")
turtle.done()
