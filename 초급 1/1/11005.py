# 11005 진법 변환 2

l = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

num, b = map(int,input().split())
answer = ""
while num != 0:
    answer += str(l[num%b])
    num //= b
    print(answer)

print(answer[::-1])