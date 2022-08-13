N = int(input())

# N = 1일 때, [0, 1], 1개 - 1
# N = 2일 때, [1, 0], 1개 - 10
# N = 3일 때, [1, 1], 2개 - 100, 101
# N = 4일 때, [2, 1], 3개 - 1000, 1001, 1010

# dp
dp = [[] for _ in range(N)]
dp[0] = [0, 1]
for i in range(1, N):
    dp[i] = [sum(dp[i-1]), dp[i-1][0]]

# 출력
print(sum(dp[-1]))