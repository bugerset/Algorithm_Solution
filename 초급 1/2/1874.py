# 1874 스택수열
import sys
n = int(sys.stdin.readline()) # 반복할 횟수

answer = [] # +,-
nl = [] # 현재 리스트에 얼마나 있는가
cnt = 0
k = 0
for i in range(n):
    num = int(sys.stdin.readline()) # 스택수열에 넣을 숫자
    while cnt < num:
        cnt += 1 
        answer.append("+")
        nl.append(cnt)

    if nl[-1] == num:
        nl.pop()
        answer.append('-')
    else:
        k = 1
    
if k == 1:
    print("NO")
else:
    for i in answer:
        print(i)