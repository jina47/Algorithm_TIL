from collections import deque as dq 

# bfs 이용
def bfs(matrix, visited, row, col):
    global N
    que = dq([[row,col]])
    cnt = 0
    while que:
        [row, col] = que.popleft()
        if visited[row][col] == False:
            visited[row][col] = True
            cnt += 1
            if row-1 >= 0 and matrix[row-1][col] == 1 and visited[row-1][col] == False:
                que.append([row-1, col]) 
            if col-1 >= 0 and matrix[row][col-1] == 1 and visited[row][col-1] == False:
                que.append([row, col-1])
            if row + 1 < N and matrix[row+1][col] == 1 and visited[row+1][col] == False:
                que.append([row+1, col])
            if col + 1 < N and matrix[row][col+1] == 1 and visited[row][col+1] == False:
                que.append([row, col+1]) 
    return [visited, cnt]


# 입력
N = int(input())
matrix = []
for _ in range(N):
    matrix.append([int(i) for i in input()])

visited = [[False for _ in range(N)] for _ in range(N)]
cnts = []
for row in range(N):
    for col in range(N):
        if matrix[row][col] == 1 and visited[row][col] == False:
            [visited, c] = bfs(matrix, visited, row, col)
            cnts.append(c)

# 출력
print(len(cnts))
cnts.sort()
for c in cnts:
    print(c)