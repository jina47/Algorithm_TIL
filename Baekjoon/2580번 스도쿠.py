from collections import deque as dq

# 입력
matrix = []
for i in range(9):
    matrix.append(list(map(int, input().split())))

lst = dq([])
for i in range(9):
    for j in range(9):
        if matrix[i][j] == 0:
            lst.append([i, j])

while lst:
    [row, col] = lst.popleft()
    

