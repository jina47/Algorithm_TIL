import sys
from collections import deque as dq

# bfs 이용
def bfs(matrix, que, N, M, H):
    dx = [0, 0, 0, 0, -1, 1]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [-1, 1, 0, 0, 0, 0]

    while que:
        [x, y, z] = que.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and matrix[nx][ny][nz] == 0:
                que.append([nx, ny, nz])
                matrix[nx][ny][nz] += matrix[x][y][z] +1       
    return matrix


# 최소 일수 계산
def day(matrix, N, M, H):
    temp = 0
    for h in range(H):
            for r in range(N):
                for c in range(M):
                    if matrix[h][r][c] == 0:
                        return -1
                    elif matrix[h][r][c] > temp:
                        temp = matrix[h][r][c]
    return temp-1



# 입력
M, N, H = map(int, sys.stdin.readline().split())
matrix = [[] for _ in range(H)]
for i in range(H*N):
    matrix[i//N].append(list(map(int, sys.stdin.readline().split())))

que = dq([])
cnt = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 0:
                cnt += 1
            elif matrix[i][j][k] == 1:
                que.append([i,j,k])


# 출력
if cnt == 0:
    print(0)
else:
    if que:
        matrix = bfs(matrix, que, N, M, H)
        print(day(matrix, N, M, H))
        
    else:
        print(-1)