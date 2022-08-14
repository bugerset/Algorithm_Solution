# 1929 소수 구하기 // 한번 풀었었음
a,b = map(int,input().split())
nl = list(range(a,b+1))

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

for i in range(len(nl)):
    if isPrime(nl[i]):
        print(nl[i])
    else:
        continue