# 9095 1,2,3 더하기

n = int(input())

for i in range(n):
    num = int(input())
    dp = [0] * (num+2)
    if num == 1:
        print(1)
    else:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for j in range(4,num+1):
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
        print(dp[num])
    
# 1 -> 1

# 2 -> 2
# 1+1 / 2

# 3 -> 4
# 1+1+1 / 1+2 / 2+1 / 3

# 4 -> 7
# 1+1+1+1 / 1+1+2 / 1+2+1 / 2+1+1 / 1+3 / 3+1 / 2+2