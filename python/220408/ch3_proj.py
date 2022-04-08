# 양수를 입력하세요
# 3으로 나누어 떨어지면 'fizz', 5로 나누어 떨어지면 'buzz', 3과 5로 나누어 떨어지면 'fizzbuzz'를 출력

num = int( input("양수를 입력하세요 : "))
while num <= 0:
    num = int( input("양수를 입력하세요 : "))
for i in range(1, num+1):
    is_3 = False
    is_5 = False
    if i % 3 == 0:
        is_3 = True
    if i % 5 == 0:
        is_5 = True
    if is_3 and is_5:
        print(f"{i} : fizzbuzz")
    elif is_3:
        print(f"{i} : fizz")
    elif is_5:
        print(f"{i} : buzz")
    else:
        print(f"{i} : *")