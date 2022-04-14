import sys
from collections import deque as dq

def dfs(matrix, start, end):
    visited = [k[:] for k in matrix]
    visited[end[0]][end[1]] = 0
    stack = [start]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while stack:
        [row, col] = stack.pop()
        if [row, col] == end:
            return visited[row][col]
    
        for i in range(4):
            nx = row + dx[i]
            ny = col + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                stack.append([nx, ny])
                visited[nx][ny] = visited[row][col] +1

    return -float('inf')



# 입력
N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append([int(i) for i in sys.stdin.readline().strip()])


# 출력
answer = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            a = dfs(matrix, [0, 0], [i, j]) + dfs(matrix, [i, j], [N-1, M-1])
            if a != -float('inf'):
                answer.append(a)

if dfs(matrix, [0, 0], [N-1, M-1]) != -float('inf'):
    answer.append(dfs(matrix, [0, 0], [N-1, M-1])+1)

if answer:
    print(min(answer))
else:
    print(-1)
    