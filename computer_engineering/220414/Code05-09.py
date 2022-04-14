import turtle
import random

## 전역 변수 선언 부분 ##
swidth, sheight = 500, 500

## 메인 코드 부분 ##
turtle.title('무지개색 원그리기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.goto(0, -sheight / 2)
turtle.pendown()
turtle.speed(15)

count = 1
for radius in range(1, 250, 11) :
    pSize = random.randrange(1, 5)
    turtle.pensize(pSize)
    if radius % 6 == 0 :
        turtle.pencolor('red')
        color = 'red'
    elif radius % 5 == 0 :
        turtle.pencolor('orange')
        color = 'orange'
    elif radius % 4 == 0 :
        turtle.pencolor('yellow')
        color = 'yellow'
    elif radius % 3 == 0 :
        turtle.pencolor('green')
        color = 'green'
    elif radius % 2 == 0 :
        turtle.pencolor('blue')
        color = 'blue'
    elif radius % 1 == 0 :
        turtle.pencolor('navyblue')
        color = 'navyblue'
    else :
        turtle.pencolor('purple')
        color = 'purple'

    turtle.circle(radius)
    print("count = %2d, radius = %3d, pSize = %2d, pencolor = %8s"%(count, radius, pSize, color))

    count += 1
    if count > 16:
        break
turtle.done()
