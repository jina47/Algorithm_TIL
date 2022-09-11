N = int(input())

dp = [0, 1, 2] + [100000 for _ in range(3, N+1)]
for i in range(3, N+1):
    # 제곱수라면 dp[i] = 1
    if i**0.5 == int(i**0.5):
        dp[i] = 1
    # 제곱수가 아니라면 i//2와 i에 가장 가까운 제곱수 중 작은 수까지 탐색해서 dp[i] 갱신
    else:
        num = min(i//2, int(int(i**0.5)**2))
        for j in range(num+1):
            dp[i] = min(dp[i], dp[j] + dp[i-j])
print(dp[N])