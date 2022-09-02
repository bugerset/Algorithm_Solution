# 11653 소인수분해
import sys

num = int(sys.stdin.readline())
k = 2

while num // k != 0:
    if num % k == 0:
        print(k)
        num //= k
    else:
        k+=1
