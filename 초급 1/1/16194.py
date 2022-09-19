# 16194 카드 구매하기 2

# 입력
n = int(input())
cp = list(map(int,input().split()))
cp.insert(0,0)

# dp생성 & 조절
dp = [0] * (n+1)
for i in range(1,n+1):
  dp[i] = cp[i]

for i in range(1,n+1):
  for j in range(1,i+1):
    dp[i] = min(dp[i], dp[i-j] + cp[j])
  
print(dp)