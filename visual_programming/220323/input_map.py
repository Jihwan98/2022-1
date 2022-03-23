"""
x, y, z = map(int, input('세 정수를 입력하시오:').split())
 
avg = (x + y + z) / 3   # 올바르게 고쳐진 계산
print("평균 =", avg) 
"""

"""
# 숫자 두 개를 입력 받아서 두 숫자의 합 계산 
a, b = input('숫자 두 개를 입력하세요: ').split()    # 입력받은 값을 공백을 기준으로 분리
sum = a + b
print('sum =', sum)
"""

"""
# 숫자 두 개를 입력 받아서 두 숫자의 합 계산 
a, b = input('숫자 두 개를 입력하세요: ').split()    # 입력받은 값을 공백을 기준으로 분리
a = int(a)    # 변수를 정수로 변환한 뒤 다시 저장
b = int(b)    # 변수를 정수로 변환한 뒤 다시 저장
sum = a + b
print('sum =', sum)
"""

"""
# 입력받은 값을 콤마를 기준으로 분리하기
a, b = map(int, input('숫자 두 개를 입력하세요: ').split(',')) # 입력받은 값을 콤마를 기준으로 분리
sum = a + b
print('sum =', sum)
"""

# 입력받은 값을 콤마를 기준으로 분리하기
a, b = map(float, input('실수 두 개를 입력하세요: ').split(',')) # 입력받은 값을 콤마를 기준으로 분리
sum = a + b
print('sum =', sum)
