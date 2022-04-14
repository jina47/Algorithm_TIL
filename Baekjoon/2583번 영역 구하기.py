def dfs(matrix, r, c):
    global answer
    stack = [[r, c]]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    while stack:
        [x, y] = stack.pop()
        if matrix[x][y] == 0:
            cnt += 1
        matrix[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == 0:
                    stack.append([nx, ny])
    answer.append(cnt)
    return matrix

M, N, K = map(int, input().split())
matrix = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for row in range(x1, x2):
        for col in range(y1, y2):
            if matrix[row][col] == 0:
                matrix[row][col] = -1
answer = []
for r in range(N):
    for c in range(M):
        if matrix[r][c] == 0:
            matrix = dfs(matrix, r, c)

answer.sort()
print(len(answer))
print(' '.join(map(str, answer)))
