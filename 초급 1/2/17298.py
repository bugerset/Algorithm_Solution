# 17298 오큰수 // 시간초과로 답 인용
import sys

l = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
stack = []
aw = [-1] * l

for i in range(l):
    while stack and num[stack[-1]] < num[i]:
        aw[stack.pop()] = num[i]
    stack.append(i)

print(*aw)