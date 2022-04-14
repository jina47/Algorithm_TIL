M, N = map(int, input().split())
maps = []
for _ in range(M):
    maps.append(list(map(int, input().split())))

dp = [[-1 for _ in range(N)] for _ in range(M)]
dp[M-1][N-1] = 1

def dfs(x, y, maps, dp):
    if dp[x][y] != -1:
        return dp[x][y]

    cnt = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if maps[nx][ny] < maps[x][y]:
                cnt += dfs(nx, ny, maps, dp)
    dp[x][y] = cnt
    return dp[x][y]

print(dfs(0,0,maps, dp))