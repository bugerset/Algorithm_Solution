# 10866 덱
import sys
n = int(sys.stdin.readline())
k = []

for i in range(n):
    cm = sys.stdin.readline().rstrip().split()
    if "push" in cm[0]:
        if "front" in cm[0]:
            k.insert(0,(cm[1]))
        else:
            k.append(cm[1])
    elif "pop" in cm[0]:
        if "front" in cm[0]:
            if len(k) == 0:
                print(-1)
            else:
                print(k[0])
                del k[0]
        else:
            if len(k) == 0:
                print(-1)
            else:
                print(k[-1])
                del k[-1]
    elif cm[0] == "size":
        print(len(k))
    elif cm[0] == "empty":
        if len(k) == 0:
            print(1)
        else:
            print(0)
    elif cm[0] == "front":
        if len(k) == 0:
            print(-1)
        else:
            print(k[0])
    elif cm[0] == "back":
        if len(k) == 0:
            print(-1)
        else:
            print(k[-1])