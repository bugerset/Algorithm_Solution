# 9613 GCD합

def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

n = int(input())

for i in range(n):
    answer = 0
    nl = list(map(int,input().split()))
    for j in range(1,nl[0]):
        for k in range(1+j,nl[0]+1):
            answer += gcd(nl[j], nl[k])
    print(answer)