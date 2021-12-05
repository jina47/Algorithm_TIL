import itertools
from collections import deque as dq

def bfs(matrix, comb, idx, virus):
    # matrix와 같은 visited 설정
    visited = [i[:] for i in matrix]
    # 벽 세우기
    for id in idx:
        [r, c] = comb[id]
        visited[r][c] = 1
    
    # 바이러스가 퍼진 후를 알기 위한 bfs
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for [r, c] in virus:
        if visited[r][c] == 2:
            que = dq([[r, c]])
            while que:
                [x, y] = que.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                        visited[nx][ny] = 2
                        que.append([nx, ny])
    # visited에 존재하는 0의 개수 return
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                cnt += 1
    return cnt

        
# 입력
N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append([int(n) for n in input().split()])

# comb에 matrix값이 0인 인덱스를 넣어줌
# virus에 matrix값이 2인 인덱스를 넣어줌
comb = []
virus = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            comb.append([i, j])
        elif matrix[i][j] == 2:
            virus.append([i, j])

# comb에서 3개를 뽑아 bfs 실행 후 0의 개수 answer에 append
answer = []
for idx in itertools.combinations(range(len(comb)), 3):
    answer.append(bfs(matrix, comb, idx, virus))
print(max(answer))
