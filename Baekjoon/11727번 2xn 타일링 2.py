n = int(input())

# n=1인 경우, 1개
# n=2인 경우, 3개
# n=3인 경우, 3+1+1

dp = [0, 1, 3]
for i in range(3, n+1):
    dp.append((dp[i-1]+2*dp[i-2])%10007)

print(dp[n])