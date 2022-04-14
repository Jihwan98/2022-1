import random

## 전역 변수 선언 부분 ##
dice1, dice2, dice3, dice4, dice5, dice6 = [0] * 6
throwCount, serialCount = 0, 0

## 메인 코드 부분 ##
if __name__ == "__main__" :
    while True :
        throwCount += 1
		
        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        dice3 = random.randrange(1, 7)
        dice4 = random.randrange(1, 7)
        dice5 = random.randrange(1, 7)
        dice6 = random.randrange(1, 7)

        if (dice1 == 1) and (dice2 == 2) and (dice3 == 3) and (dice4 == 4) and (dice5 == 5) and (dice6 == 6) :
            break

    print('6개가 주사위 숫자가 순서대로 나올 때까지 주사위를 던진 횟수 -->', throwCount)
    print('6개의 주사위 숫자 순서대로 -->', dice1, dice2, dice3, dice4, dice5, dice6)