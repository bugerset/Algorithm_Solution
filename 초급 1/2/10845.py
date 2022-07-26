# 10845 큐
import sys
n = int(sys.stdin.readline())
k = []

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        k.append(command[1])
    elif command[0] == "pop":
        if len(k) == 0:
            print(-1)
        else:
            print(k[0])
            del k[0]
    elif command[0] == "size":
        print(len(k))
    elif command[0] == "empty":
        if len(k) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(k) == 0:
            print(-1)
        else:
            print(k[0])
    elif command[0] == "back":
        if len(k) == 0:
            print(-1)
        else:
            print(k[-1])