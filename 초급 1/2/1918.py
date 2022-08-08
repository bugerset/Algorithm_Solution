# 1918 후위 표기식 // 보류
import sys
view = list(sys.stdin.readline().rstrip())
stack = []
answer = []
for i in view:
    if i.isalpha():
        answer += i

    else:
        if i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(i)
