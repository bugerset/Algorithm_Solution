# dp공부
n = int(input())
food = list(map(int, input().split()))

# 작은 문제부터 해결해서 저장할 dp테이블
dp = [0]*100

# 다이나믹 프로그래밍(bottom up)
dp[0] = food[0]
dp[1] = food[1]

for i in range(n):
    dp[i]=max(dp[i-1], dp[i-2]+food[i])

print(dp[n-1])