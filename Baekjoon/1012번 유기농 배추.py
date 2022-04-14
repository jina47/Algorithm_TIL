from collections import deque as dq

# bfs 이용
def bfs(matrix, visited, row, col):
    global N, M
    que = dq([[row, col]])
    while que:
        [r, c] = que.popleft()
        if visited[r][c] == False:
            visited[r][c] = True
            if r-1 >= 0 and matrix[r-1][c] == 1 and visited[r-1][c] == False:
                que.append([r-1, c])
            if c-1 >= 0 and matrix[r][c-1] == 1 and visited[r][c-1] == False:
                que.append([r, c-1])
            if r+1 < N and matrix[r+1][c] == 1 and visited[r+1][c] == False:
                que.append([r+1, c])
            if c+1 < M and matrix[r][c+1] == 1 and visited[r][c+1] == False:
                que.append([r, c+1])
    return visited


# 입력
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        col, row = map(int, input().split())
        matrix[row][col] = 1
    
    visited = [[False for _ in range(M)] for _ in range(N)]
    cnt = 0
    for row in range(N):
        for col in range(M):
            if matrix[row][col] == 1 and visited[row][col] == False:
                visited = bfs(matrix, visited, row, col)
                cnt += 1
    print(cnt)

