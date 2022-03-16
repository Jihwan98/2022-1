seconds = int(input("초를 입력하세요 : "))

hour = seconds // (60 * 60)
remain_second = seconds % (60 * 60)

minute = remain_second // 60
remain_second = remain_second % 60

print(f"입력한 시간은 {hour}시간 {minute}분 {remain_second}초 입니다.")