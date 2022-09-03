import sys
from collections import deque as dq
    
# 입력
N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append([int(i) for i in sys.stdin.readline().strip()])


# [벽을 안 부순 경우 최단 거리, 벽을 한 번 부순 경우 최단 거리]를 담는 visited
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 초깃값
que = dq([[0, 0, 0]])
visited[0][0][0] = 1

# bfs 실행
while que:
    cnt, x, y = que.popleft()
    # 목적지 도달시 break
    if x == N-1 and y == M-1:
        break
    
    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            # 벽을 한 번도 안 부순 경우
            if cnt == 0:
                # 다음 칸이 벽이 아닌 경우
                if matrix[nx][ny] == 0 and visited[nx][ny][0] == 0:
                    que.append([0, nx, ny])
                    visited[nx][ny][0] = visited[x][y][0] + 1
                # 다음 칸이 벽인 경우
                elif matrix[nx][ny] == 1 and visited[nx][ny][1] == 0:
                    # 벽을 한 번 부수게 되므로 [1, nx, ny]를 que에 넣어줌
                    que.append([1, nx, ny])
                    visited[nx][ny][1] = visited[x][y][0] + 1

            # 벽을 한 번 부순 경우 다음 칸은 벽이 아니어야 함
            elif cnt == 1 and matrix[nx][ny] == 0 and visited[nx][ny][1] == 0:
                que.append([1, nx, ny])
                visited[nx][ny][1] = visited[x][y][1] + 1


# 벽을 안 부순 경우와 벽을 한 번이라도 부순 경우 모두 이동 가능하면 최단 거리 출력                    
if visited[N-1][M-1][0] != 0 and visited[N-1][M-1][1] != 0:
    print(min(visited[N-1][M-1]))
# bfs 실행 후 목적지에 도달할 수 없으면 -1 출력
elif visited[N-1][M-1] == [0, 0]:
    print(-1)
# 둘 중에 하나의 경우만 가능하면 0이 아닌 최단 거리만 출력
else:
    print(max(visited[N-1][M-1]))