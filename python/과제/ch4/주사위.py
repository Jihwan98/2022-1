import random

def dice_game():
    input("[Enter]키를 눌러 주사위 번호를 선택합니다.")
    me = random.randint(1, 6)
    com = random.randint(1, 6)
    print("인간 : 주사위값 =", me)
    print("컴퓨터 : 주사위값 =", com)
    if me > com:
        print("인간승리")
    elif me < com:
        print("컴퓨터승리")
    else:
        print("비겼습니다.")

def main():
    while True:
        dice_game()
        key = input("중단할까요(Y/N)?")
        if key == 'Y' or key == 'y':
            print("주사위 게임을 종료합니다.")
            break

print('주사위 게임을 시작합니다.')
main()