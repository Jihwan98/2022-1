a = int(input("첫 번째 숫자를 입력하세요, a = : "))
b = int(input("두 번째 숫자를 입력하세요, b = : "))
result = a + b
print(a, "+", b, "=", result)
result = a - b
print(a, "-", b, "=", result)
result = a * b
print(a, "*", b, "=", result)
result = a / b
print(a, "/", b, "=", result)
result = a // b # 몫 
print(a, "//", b, "=", result)
result = a % b # 나머지 
print(a, "%", b, "=", result)
result = a ** b # 제곱 계산  
print(a, "**", b, "=", result)
print(a, "**", b, "=", pow(a, b))
print("pow(",a, ",", b, ") =", pow(a, b))
