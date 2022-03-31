import turtle
t = turtle.Turtle()
t.shape("turtle")

for i in range(3):
    t.forward(100)
    t.left(360/3)

for i in range(4):
    t.forward(100)
    t.left(360/4)

for i in range(6):
    t.forward(100)
    t.left(360/6)

turtle.done()