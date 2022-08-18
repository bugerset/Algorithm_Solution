# 2004 조합 0의 개수
import sys
sys.setrecursionlimit(10**6)

def fac(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fac(n-1)

a,b = map(int,input().split())
cnt = 0
k=list(str(int(fac(a)/(fac(a-b)*fac(b)))))

for i in range(len(k)-1,-1,-1):
    if k[i] == "0":
        cnt += 1
    else:
        print(cnt)
        break
