# 6588 골드바흐의 추측
import sys

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2,int(num**0.5+1)):
            if num%i == 0:
                return False
        return True

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(3,n,1):
        if isPrime(i):
            if isPrime(n-i):
                print("{} = {} + {}".format(n,i,n-i))
                break