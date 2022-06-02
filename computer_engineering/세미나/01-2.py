# 코드 설명 : 리스트 aa에 0부터 2씩 증가한 100개의 수를 추가하고, 리스트 aa 값의 역순으로 리스트 bb에 값을 추가한다.

aa = []  
bb = []    

for i in range(0, 200, 2) :    
    aa.append(i)     
    
for i in range(len(aa)-1, -1, -1) :   
    bb.append(aa[i])  

print("bb[0]에는 %d이, bb[99]에는 %d이 입력됩니다." % (bb[0], bb[99]))