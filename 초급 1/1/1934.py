# 1934 최소 공배수
def c(a,b):
    while b>0:
        a,b=b,a%b
    return a
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(int(a*b/c(a,b)))