# 10828 스택
import sys
n = int(sys.stdin.readline())
stack = []

for i in range(n):
    command = sys.stdin.readline().split() # command $
    if "push" in command: # push가 명령어라면
        stack.append(int(command[1])) # $를 추가
    elif "pop" in command: # pop이 명령어면
        if len(stack) > 0:
            print(stack.pop()) # 출력과 함께 삭제
        else:
            print(-1) # 아무것도 없으면 -1출력
    elif "size" in command: # size가 명령어면
        print(len(stack)) # 사이즈 출력
    elif "empty" in command: # empty가 명령어면
        if len(stack) < 1: # 아무것도 없다면
            print(1) # 1출력
        else: # 아니면
            print(0) # 0출력
    elif "top" in command: # top이 명령어라면
        if len(stack) < 1: # 아무것도 없으면
            print(-1) # -1출력
        else: # 뭐라도 있다면
            print(stack[-1]) # 맨 위에있는 수 출력