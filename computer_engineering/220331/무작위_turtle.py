import turtle
import random
rand_turtle = turtle.Turtle()
rand_turtle.shape('turtle')
for count in range(10):
    rand_turtle.forward(random.randint(1,100))
    rand_turtle.setheading(random.randint(0,360))
turtle.done()