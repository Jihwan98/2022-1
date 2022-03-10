import turtle

turtle.penup()

turtle.goto(-39, 48) 
turtle.pendown()
turtle.write("(-39, 48)")
turtle.goto(50, -50) 
turtle.write("(50, -50)")
turtle.penup()

turtle.pencolor('red')
turtle.goto(-39 + 80, 48) 
turtle.pendown()
turtle.write(f"({-39 + 80}, 48)")
turtle.goto(50 + 80, -50) 
turtle.write(f"({50 + 80}, -50)")
turtle.penup()

turtle.pencolor('blue')
turtle.goto(-39 + 80 + 90, 48) 
turtle.pendown()
turtle.write(f"({-39 + 80 + 80}, 48)")
turtle.goto(50 + 80 + 80, -50) 
turtle.write(f"({50 + 80 + 80}, -50)")

turtle.done()