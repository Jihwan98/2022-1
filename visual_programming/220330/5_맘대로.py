# code04-02.py 
import turtle
import random
## 전역 변수 선언 부분 ##
swidth, sheight, pSize, exitCount = 300, 300, 3, 0
r, g, b, angle, dist, curX, curY = [0] * 7
## 메인 코드 부분 ##
turtle.title('거북이가 맘대로 다니기')
turtle.shape('turtle')
turtle.pensize(pSize) # 수정 가능 3-> 2
turtle.setup(width=swidth+30, height=sheight+30)
turtle.screensize(swidth, sheight)
while True :
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))  # pencolor 설정 
    
    angle =  random.randrange(0,360)
    dist = random.randrange(1,100) # 수정 필요 100 -> 50
    turtle.left(angle) #  angle 설정
    turtle.forward(dist) # 길이, dist 설정
    curX = turtle.xcor() # x- 좌표
    curY = turtle.ycor() # y- 좌표
    if (-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight / 2<= curY and curY <= sheight / 2) :
        pass
    else :
        turtle.penup()
        turtle.goto( 0, 0 )
        turtle.pendown()
        
        exitCount += 1
        if exitCount >= 5:
            break

turtle.done()