# 도전문제 4.9

import random

player1 = input("player1 : ")
player2 = input("player2 : ")

print("주사위 게임을 시작합니다.")
p1 = random.randrange(1, 7)
p2 = random.randrange(1, 7)

print(f"{player1} : {p1}")
print(f"{player2} : {p2}")

if p1 > p2:
    print(f"{player1}이/가 이겼습니다.")
elif p1 < p2:
    print(f"{player2}이/가 이겼습니다.")
else:
    print("무승부입니다.")
print("게임이 종료되었습니다.")