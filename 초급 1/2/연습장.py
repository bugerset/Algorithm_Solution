default = [1,1,2,2,2,8]

hand = list(map(int,input().split()))

for i in range(6):
    if hand[i] > default[i]:
        print(-(hand[i]-default[i]),end=" ")
    else:
        print(default[i]-hand[i],end=" ")