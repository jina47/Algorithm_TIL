from collections import deque as dq
import sys
# 세로 N 가로 M
N, M = map(int, input().split())
# 영상
img = []
for _ in range(N):
    img.append(list(map(int, sys.stdin.readline().split())))
# 경계값 T
T = int(input())

# 새로운 화면
newimg = [[] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if (img[i][3*j] + img[i][3*j+1] + img[i][3*j+2])/3 >= T:
            newimg[i].append(255)
        else:
            newimg[i].append(0)

# 방문 처리
visited = [[0 for _ in range(M)] for _ in range(N)]
# bfs
def bfs(r, c):
    que = dq([[r,c]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while que:
        [x, y] = que.popleft()
        visited[x][y] = 1
        for id in range(4):
            nx = x + dx[id]
            ny = y + dy[id]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                # 물체에 해당되면 que에 append, 방문처리
                if newimg[nx][ny] == 255:
                    que.append([nx, ny])
                    visited[nx][ny] = 1

# 물체 개수 cnt
cnt = 0
for r in range(N):
    for c in range(M):
        # 값이 255인데 visited값이 0이면 새로운 물체이므로 bfs
        if newimg[r][c] == 255 and visited[r][c] == 0:
            cnt += 1
            bfs(r, c)

print(cnt)
