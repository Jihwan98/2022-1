# 코드 설명 : 리스트 aa에 0부터 2씩 증가한 100개의 수를 추가하고, 리스트 aa 값의 역순으로 리스트 bb에 값을 추가한다.

aa = []     # 빈 리스트 생성
bb = []     # 빈 리스트 생성
value = 0   # 초기 변수 선언

for i in range(0, 100) :    # 100번 반복
    aa.append(value)        # 리스트aa에 value 추가
    value += 2              # value 2씩 증가 (짝수)

for i in range(0, 100) :    # 100번 반복
    bb.append(aa[99 - i])   # 리스트bb에 리스트aa의 인자를 역순으로 추가

print("bb[0]에는 {}이, bb[99]에는 {}이 입력됩니다.".format(bb[0], bb[99]))