# 10872 팩토리얼

# 1번 풀이
def fac(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fac(n-1)

print(fac(int(input())))

# 2번 풀이
# n = int(input())
# ans = 1

# for i in range(1,n+1):
#     ans *= i
    
# print(ans)

# 3번 풀이

# n = int(input())
# ans = 1

# while n != 1:
#     ans *= n
#     n -= 1

# print(ans)