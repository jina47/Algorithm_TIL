from collections import deque as dq
import sys
N = int(input())

# 게임판 maps
maps = []
for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().split())))

# 방문 처리
visited = [[0 for _ in range(N)] for _ in range(N)]

# bfs
que = dq([[0, 0]])
while que:
    [x, y] = que.popleft()
    visited[x][y] = 1
    # 끝 인덱스에 도달시 break
    if x == N-1 and y == N-1:
        break
    # go는 이동할 칸의 개수
    go = maps[x][y]
    # 오른쪽과 아래로만 이동 가능
    dx = [go, 0]
    dy = [0, go]
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        # maps를 벗어나지 않고 방문하지 않은 칸이라면 que에 append
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            que.append([nx, ny])

# 끝에 도착할 수 있으면 'HaruHaru' 출력 그렇지 않으면 'Hing' 출력
if visited[-1][-1] == 1:
    print('HaruHaru')
else:
    print('Hing')
