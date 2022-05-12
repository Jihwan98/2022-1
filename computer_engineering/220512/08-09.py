# solution08-09-01.py
import turtle
import random
from tkinter.simpledialog import *
import math
## 전역 변수 선언 부분 ##
inStr = ''
swidth, sheight=300, 300
tX, tY, txtSize  = [0] * 3
## 메인 코드 부분 ##
turtle.title('거북이가 원 모양의 글자쓰기')
turtle.shape('turtle')
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth, sheight)    
turtle.penup()
inStr = askstring('문자열 입럭', '거북이가 쓸 문자열을 입력')
dist= 100
angle = 0
value = int( 360 / len(inStr)) # 360를 문자열의 개수로 나눈다.
for  ch  in inStr :
    rad = 3.141592 * angle / 180
    tX = dist * math.cos(rad)
    tY = dist * math.sin(rad)
    angle += value
    r = random.random() ; g = random.random(); b = random.random()
    txtSize =  random.randrange(20, 21)
    turtle.goto(tX,tY)
    
    turtle.pencolor( (r,g,b) )
    turtle.write(ch, font=('맑은고딕', txtSize, 'bold'))
            
turtle.hideturtle() # add 
turtle.done()