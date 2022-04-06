score = int(input("점수를 입력하세요 : "))

"""
if score >= 90 :
        level = "A"
        # print("A", end="")
else :
        if score >= 80 :
                level = "B"
                # print("B", end="")
        else :
                if score >= 70 :
                        level = "C"
                        # print("C", end="")
                else :
                        if score >= 60 :
                                level = "D"
                                # print("D", end="")
                        else :
                                level = "F"
                                # print("F", end="")
"""
"""
if score >= 90 :
    level = "A"
elif score >= 80 :
    level = "B"
elif score >= 70 :
    level = "C"
elif score >= 60 :
    level = "D"
else :
    level = "F"
"""

if score >= 95 :
    level = "A+"
elif score >= 90:
    level = "A"
elif score >= 85:
    level = "B+"
elif score >= 80 :
    level = "B"
elif score >= 75:
    level = "C+"
elif score >= 70 :
    level = "C"
elif score >= 65:
    level = "D+"
elif score >= 60 :
    level = "D"
else :
    level = "F"

print(level, "학점입니다. ^^")