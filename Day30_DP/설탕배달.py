n = int(input())

dp = [float('inf')] * (n+1)
dp[0] = 0  # 0kg은 봉지 0개

for i in range(1, n+1):
    if i >= 3 and dp[i-3] != float('inf'):
        dp[i] = min(dp[i], dp[i-3] + 1)  # 3kg 봉지 추가
    if i >= 5 and dp[i-5] != float('inf'):
        dp[i] = min(dp[i], dp[i-5] + 1)  # 5kg 봉지 추가

print(-1 if dp[n] == float('inf') else dp[n])