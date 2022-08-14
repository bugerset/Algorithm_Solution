# 11656 접미사 배열
w=input()
k=[]

for i in range(len(w)):
    k.append(w[i:])
k.sort()
for i in range(len(k)):
    print(k[i])