# 11576 Base Conversion

A,B = map(int,input().split())
m = int(input())
n = list(map(int,input().split()))[::-1]

k = 0

answer = []

for i in range(m):
    k += n[i]*(A**i)

while k != 0:
    answer.append(str(k%B))
    k //= B

answer.reverse()

print(" ".join(answer))