# 1978 소수 찾기 // 한번 풀었었음

n = int(input())
nl = list(map(int,input().split()))
cnt = 0

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

for i in range(n):
    if isPrime(nl[i]):
        cnt += 1
print(cnt)