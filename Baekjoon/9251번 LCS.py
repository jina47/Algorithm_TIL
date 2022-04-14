import sys

first = ' ' + sys.stdin.readline().strip()
second = ' ' + sys.stdin.readline().strip()

dp = [[0 for _ in range(len(second))] for _ in range(len(first))]
for i in range(1, len(first)):
    for j in range(1, len(second)):
        if first[i] == second[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
print(max(dp[-1]))

