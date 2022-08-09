# 1918 후위 표기식
import sys
view = list(sys.stdin.readline().rstrip())
stack = []
answer = []

for i in view:
    if i == "(":
        stack.append(i)
    elif i == "+" or i == "-":
        while stack and stack[-1] != '(':
            answer.append(stack.pop())
        stack.append(i)
    elif i == "*" or i == "/":
        while stack and (stack[-1] == "*" or stack[-1] == "/"):
            answer.append(stack.pop())
        stack.append(i)
    elif i == ")":
        while True:
            if stack and stack[-1] != "(":
                answer.append(stack.pop())
            else:
                stack.pop()
                break
    else:
        answer.append(i)

stack.reverse()
answer.extend(stack)
print("".join(answer))