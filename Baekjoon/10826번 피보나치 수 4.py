# 피보나치 수 구하기
N = int(input())
dp = [0 for _ in range(N+1)]

# N이 0이 아닌 경우
if N != 0:
    dp[1] = 1
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]

print(dp[N])