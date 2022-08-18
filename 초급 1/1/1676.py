# 1676 팩토리얼 0의 개수
n = int(input())
ans = 1
k = []
cnt = 0

for i in range(1,n+1):
    ans *= i

ans = str(ans)

for i in ans:
    k.append(i)

for i in range(len(k)-1,-1,-1):
    if k[i] == "0":
        cnt += 1
    else:
        print(cnt)
        break