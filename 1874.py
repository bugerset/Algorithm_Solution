# 1874 스택수열
import sys
n = int(sys.stdin.readline()) # 반복할 횟수

answer = [] # +,-
nl = [] # 현재 리스트에 얼마나 있는가
cl = [0] # 최고로 넣은 숫자 저장장치

for i in range(n):
    num = int(sys.stdin.readline()) # 스택수열에 넣을 숫자
    while True:
        if (num not in nl):
            cl[0] += 1
            answer.append("+")
            nl.append(cl[0])
            if len(nl) > num:
                break
        elif num in nl:   
            answer.append("-")
            if nl.pop() == num:
                break

if len(nl) > num:
    print("NO")
else:
    for i in answer:
        print(i)