import turtle
t = turtle.Turtle()
# 거북이의 속도는 0으로 설정하면 최대가 된다. 
t.speed(0)
t.width(3)
length = 10      # 초기 선의 길이는 10으로 한다. 
# while 반복문이다. 선의 길이가 500보다 작으면 반복한다.  
while length < 500:    
    t.forward(length)             # length만큼 전진한다. 
    t.right(360/3)
    length += 5  # 선의 길이를 5만큼 증가시킨다.

turtle.done()