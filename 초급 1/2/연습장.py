import sys
n = int(sys.stdin.readline())
k = [0]*10001

for i in range(n):
    num = int(sys.stdin.readline())
    k[num-1] += 1

for i in range(0,10001):
    for j in range(k[i]):
        print(i+1)