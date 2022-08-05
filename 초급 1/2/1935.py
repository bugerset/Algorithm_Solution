# 1934 후위 표기식 2 // 답 인용
import sys
n = int(sys.stdin.readline()) # 횟수
view = list(sys.stdin.readline().rstrip())
stack = [] # 스택
alpha = [0] * n

for i in range(n):
    alpha[i] = int(sys.stdin.readline())

for i in view:
    if i.isalpha():
        stack.append(alpha[ord(i) - ord("A")])
    else:
        p1 = stack.pop()
        p2 = stack.pop()
        if i == "+":
            stack.append(p1+p2)
        elif i == "-":
            stack.append(p2-p1)
        elif i == "*":
            stack.append(p1*p2)
        elif i == "/":
            stack.append(p2/p1)

print(format(stack[0], ".2f"))