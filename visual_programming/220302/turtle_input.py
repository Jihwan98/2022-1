import turtle
num = int(input("몇 각형을 원합니까? : "))
if num < 3:
    print("3 보다 큰 수를 입력해 주세요")
    quit()
t = turtle.Turtle()
t.shape('turtle')
angle = 360 / num
line = int(600/num)
for i in range(num):
    t.forward(line)
    t.left(angle)

turtle.done()
