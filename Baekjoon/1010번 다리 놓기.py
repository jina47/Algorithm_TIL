# 테스트 케이스
T = int(input())

dp = [[1 for _ in range(i+1)] for i in range(31)]

for _ in range(T):
    w, e = map(int, input().split())
    for i in range(2, e+1):
        for j in range(1, i):
            if dp[i][j] == 1:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    print(dp[e][w])

    
    