## 변수 선언 부분 ##
money, c50, c10, c5, c1 = 0,0,0,0,0
## 메인 코드 부분 ##
money=int(input("교환할 돈은 얼마 ? "))
c50 = money // 50000
money %= 50000
print("\n50000원짜리 = %3d, 잔돈 1- money = %6d" %(c50, money))

c10 = money // 10000
money %= 10000
print("\n10000원짜리 = %3d, 잔돈 2- money = %6d" % (c10, money))

c5 = money // 5000
money %= 5000
print("\n5000원짜리 = %3d, 잔돈 2- money = %6d" % (c5, money))

c1 = money // 1000
money %= 1000
print("\n1000원짜리 = %3d, 잔돈 2- money = %6d" % (c1, money))