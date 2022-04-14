# B -> BA, A -> B
K = int(input())
dp = [[] for _ in range(K+1)]
dp[0] = [1, 0]
dp[1] = [0, 1]

# i의 A, B 개수는 i-1의 A, B의 개수와 i-2의 A, B의 개수를 더해주면 됨
for i in range(2,K+1):
    dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1]+dp[i-2][1]]

print(dp[K][0], dp[K][1])
