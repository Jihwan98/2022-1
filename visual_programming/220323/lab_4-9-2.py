import turtle 
t = turtle.Turtle() 
t.shape("turtle") 
 
x1, y1 = map(int, turtle.textinput("", "왼쪽 하단 모서리 좌표 x, y :").split())
x2, y2 = map(int, turtle.textinput("", "오른쪽 상단 모서리 좌표 x, y :").split())
t.penup()
t.goto(x1, y1)
t.pendown()
t.goto(x2, y1)
t.goto(x2, y2)
t.goto(x1, y2)
t.goto(x1, y1)
x, y = map(int, turtle.textinput("", "점의 좌표 x, y :").split())
t.penup()
t.width(50)
t.goto(x, y)
t.pendown()
t.forward(1)
if (x > x1 and x < x2) and (y > y1 and y < y2):
    t.write("점은 사각형의 내부에 있습니다")
else:
    t.write("점은 사각형의 외부에 있습니다")
turtle.done()
