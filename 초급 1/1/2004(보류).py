# 2004 조합 0의 개수 // 답 인용

def counting(n, k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt

a,b = map(int,input().split())

five_c = counting(a,5) - counting(b,5) - counting(a-b,5)
two_c = counting(a,2) - counting(b,2) - counting(a-b,2)

print(min(five_c,two_c))