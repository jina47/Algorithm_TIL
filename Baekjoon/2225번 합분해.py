# 입력
N, K = map(int, input().split())

# K가 1일 때 dp
dp = [1 for _ in range(N+1)]
# K가 2 이상일 때
for _ in range(2, K+1):
    # new_dp는 K번째 dp
    new_dp = [0 for _ in range(N+1)]
    # new_dp[i] = sum(dp[0] + .. dp[i])
    for i in range(N+1):
        if i == 0:
            new_dp[0] = 1
        # new_dp[i] = new_dp[i-1] + dp[i]    
        else:
            new_dp[i] = (new_dp[i-1] + dp[i]) % 1000000000
    dp = new_dp

# 1000000000으로 나눈 나머지 출력
print(dp[N] % 1000000000)