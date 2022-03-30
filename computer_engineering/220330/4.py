## 변수 선언 부분 ##
money, c500, c100, c50, c10 = 0, 0, 0, 0, 0
## 메인 코드 부분 ##
money=int(input("교환할 돈은 얼마 ? "))
c500 = money // 500
money %= 500
print("\nc500 = %3d, 잔돈 1- money =%4d" %(c500, money))
c100 = money // 100
money %= 100
print("c100 = %3d, 잔돈 2- money =%4d" %(c100, money))
c50 = money // 50
money %= 50
print("c50  = %3d, 잔돈 3- money =%4d" %(c50, money))
c10 = money // 10
money %= 10
print("c10  = %3d, 잔돈 4- money =%4d" %(c10, money))
