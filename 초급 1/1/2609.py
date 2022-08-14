# 2609 최대공약수와 최소공배수
A,B = map(int,input().split())

def chleo(A,B):
    while B>0:
        A,B=B,A%B
    return A
print(chleo(A,B))
print(int(A*B/chleo(A,B)))