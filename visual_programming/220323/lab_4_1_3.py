#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 4-1 입력 숫자에 따라 터틀 그래픽을 제어해보자, 98쪽
#
import turtle

t = turtle.Turtle()
t.shape("turtle")

t.penup()  # 펜을 올려서 그림이 그려지지 않게 한다.
t.goto(90, 0)  
t.write("x > y")
t.goto(-110, 0)
t.write("y > x")
t.goto(-10, 100)
t.write("x = y")


t.goto(0, 0)  # (0, 0) 위치로 거북이를 이동시킨다.
t.pendown()  # 펜을 내려서 그림이 그려지게 한다.

x = int(turtle.textinput("", "첫 번째 숫자를 입력하시오 :"))
y = int(turtle.textinput("", "두 번째 숫자를 입력하시오 :"))


if x > y:
    t.goto(100, 0)
elif x < y:
    t.goto(-100, 0)
elif x == y:
    t.goto(0, 100)

turtle.done()