aa = []
bb = []
value = 0

for i in range(0,200) :
    aa.append(value)
    value += 3

for i in range(len(aa)-1, -1, -1) :
    bb.append(aa[i])

print(" bb[0]에는 {}이, bb[199]에는 {}이 입력됩니다.".format(bb[0], bb[199]))