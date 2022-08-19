# 17087 숨바꼭질 6
import sys

def gcd(a,b):
    while b>0:
        a,b = b,a%b
    return a

n,s = map(int,sys.stdin.readline().rstrip().split())
nl = list(map(int,sys.stdin.readline().rstrip().split()))
k = list(abs(nl[i]-s) for i in range(n))
m = min(k)

for i in range(len(k)): 
    m = gcd(m,k[i])
    
print(m)