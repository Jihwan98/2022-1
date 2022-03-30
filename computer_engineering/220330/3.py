a = int(input("첫 번째 숫자를 입력하세요, a = : "))
b = int(input("두 번째 숫자를 입력하세요, b = : "))
result = a + b
print("{:2d} + {:2d} = {:6d}".format( a, b, result))
result = a - b
print("{:2d} - {:2d} = {:6d}".format( a, b, result))
result = a * b
print("{:2d} * {:2d} = {:6d}".format( a, b, result))
result = a / b
print("{:2d} / {:2d} = {:6.3f}".format( a, b, result)) # floating point 
result = a // b # 몫 
print("{:2d} //{:2d} = {:6d}".format( a, b, result))
result = a % b # 나머지 
print("{:2d} %% {:2d} = {:6d}".format( a, b, result)) # 2개의 %% 사용
result = a ** b # 제곱 계산  
print("{:2d} **{:2d} = {:6d}".format( a, b, result))
print("{:2d} **{:2d} = {:6d}".format( a, b, pow(a, b)))