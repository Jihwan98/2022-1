import turtle

x1, y1 = map(int, input("Enter the first point x1, y1: ").split())
x2, y2 = map(int, input("Enter the first point x2, y2: ").split())

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.pensize(1)
turtle.write("p1(" + str(x1) + ", " + str(y1) + ")")
turtle.goto(x2, y2)
turtle.write("p2(" + str(x2) + ", " + str(y2) + ")")
turtle.hideturtle() # turtle을 숨긴다.
turtle.done()
