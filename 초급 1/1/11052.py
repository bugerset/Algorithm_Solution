# 11052 카드 구매하기

n = int(input()) # 몇장?

cp = list(map(int,input().split())) # 카드 리스트 목록
cp.insert(0,0) # cp의 첫번째에 0을 삽입

dp = [0] * (n+1) # dp리스트 생성

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], dp[i-j] + cp[j]) # 전꺼를 일일이 검사하면서
        # 만약 i = 3일때,
        # dp[2] + cp[1]이 크면 dp[3]으로
        # dp[1] + cp[2]가 크면 dp[3]으로
        # dp[0] + cp[3]이 크면 dp[3]으로

print(dp[n])