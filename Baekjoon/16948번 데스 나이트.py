from collections import deque as dq
# 체스판의 크기
N = int(input())
r1, c1, r2, c2 = map(int, input().split())

# 이동횟수
cnt = [[-1 for _ in range(N)] for _ in range(N)]
cnt[r1][c1] = 0
# bfs
que = dq([[r1, c1]])
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
while que:
    [x, y] = que.popleft()
    # 목적지에 다다르면 break
    if x == r2 and y == c2:
        break
    # 데스나이트가 이동할 수 있는 곳 찾기
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and cnt[nx][ny] == -1:
            que.append([nx, ny])
            cnt[nx][ny] = cnt[x][y] + 1

# 출력
print(cnt[r2][c2])