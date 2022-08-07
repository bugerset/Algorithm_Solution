# 1934 후위 표기식 2 // 답 인용

import sys
n = int(sys.stdin.readline()) # 횟수
view = list(sys.stdin.readline().rstrip()) # 후위 표기식 생성
stack = [] # 스택 생성
alpha = [0] * n # 알파벳에 대응하는 숫자를 넣어주기 위한 리스트 생성

for i in range(n): # 횟수만큼 돌린다
    alpha[i] = int(sys.stdin.readline()) # alpha[i]에 넣을 숫자 생성

for i in view:
    if i.isalpha(): # 알파벳이면
        # A면 0이므로 첫번째, B면 1이므로 두번째
        stack.append(alpha[ord(i) - ord("A")]) # ord로 구하기
    else: # 알파벳이 아니라 기호면
        p1 = stack.pop() # 스택에 있는 마지막 수를 뺀다
        p2 = stack.pop() # 한번 빠진 스택에 있는 마지막 수를 뺀다
        if i == "+":
            stack.append(p1+p2)
        elif i == "-":
            stack.append(p2-p1)
        elif i == "*":
            stack.append(p1*p2)
        elif i == "/":
            stack.append(p2/p1)

print(format(stack[0], ".2f")) # format으로 두번째 소수까지 생성