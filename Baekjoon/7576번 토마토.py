from collections import deque as dq
import sys

# bfs 이용
def bfs(matrix, que, N, M):
    while que:    
        [row, col] = que.popleft()
        number = matrix[row][col]
        if matrix[row][col] >= 1:
            # matrix[행][열]의 상하좌우 중에 0이 있으면 que에 없는 것이므로 append
            # matrix[행][열]의 상하좌우 값은 matrix[행][열]의 값에 1을 더해줌  
            if row-1 >= 0 and matrix[row-1][col] == 0:
                que.append([row-1, col])
                matrix[row-1][col] = number+1
            if col-1 >= 0 and matrix[row][col-1] == 0:
                que.append([row, col-1])
                matrix[row][col-1] = number+1
            if row+1 < N and matrix[row+1][col] == 0:
                que.append([row+1, col])
                matrix[row+1][col] = number+1
            if col+1 < M and matrix[row][col+1] == 0:
                que.append([row, col+1])
                matrix[row][col+1] = number+1
    return matrix


# 입력
M, N = map(int, sys.stdin.readline().split())
matrix = []
que = dq([])
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

cnt = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            cnt += 1
        elif matrix[i][j] == 1:
            que.append([i, j])

# 출력
# matrix에 0이 없으면 더 익을 토마토가 없으므로 0 출력
if cnt == 0:
    print(0)
else:
    # que에 값이 있으면 전체 토마토를 익힐 수 있는 가능성이 있으므로 bfs 실행
    if que:
        day = 0
        matrix = bfs(matrix, que, N, M)
        # matrix에 0이 남아있다면 전체를 다 익히지 못한 것이므로 -1 출력
        for i in range(N):
            if 0 in matrix[i]:
                day = -1
                print(day)
                break
        # matrix에 0이 없다면 전체 다 익힌 것이므로 matrix의 최대값에 1을 뺀 값 출력
        if day != -1:
            print(max(map(max, matrix))-1)    
    
    # que에 값이 없으면 익은 토마토가 없어서 전체 토마토를 익힐 수 없으므로 -1 출력
    else:
        print(-1)
    
