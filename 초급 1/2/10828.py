# 10828 스택
import sys
n = int(sys.stdin.readline())
stack = []

for i in range(n):
    command = sys.stdin.readline().split()
    if "push" in command:
        stack.append(int(command[1]))
    elif "pop" in command:
        if len(stack) > 0:
            print(stack[-1])
            del stack[-1]
        else:
            print(-1)
    elif "size" in command:
        print(len(stack))
    elif "empty" in command:
        if len(stack) < 1:
            print(1)
        else:
            print(0)
    elif "top" in command:
        if len(stack) < 1:
            print(-1)
        else:
            print(stack[-1])