from collections import deque as dq
import sys

# bfs 이용
def bfs(matrix, visited):
    global N, M
    row, col = 0, 0
    que = dq([[0,0]])
    while que:
        [r, c] = que.popleft()
        if visited[r][c] == False:
            visited[r][c] = True
            temp = []
            if c+1 < M and matrix[r][c+1] != 0:
                if visited[r][c+1] == False:
                    que.append([r, c+1])
                else:
                    temp.append(matrix[r][c+1])
            if r+1 < N and matrix[r+1][c] != 0:
                if visited[r+1][c] == False:
                    que.append([r+1, c])
                else:
                    temp.append(matrix[r+1][c])
            if c-1 >= 0 and matrix[r][c-1] != 0:
                if visited[r][c-1] == False:
                    que.append([r, c-1])
                else:
                    temp.append(matrix[r][c-1])
            if r-1 >= 0 and matrix[r-1][c] != 0 :
                if visited[r-1][c] == False:
                    que.append([r-1, c])
                else:
                    temp.append(matrix[r-1][c])
            if temp:
                matrix[r][c] = min(temp) + 1

            if r == N-1 and c == M-1:
                return matrix[r][c]


#입력
N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append([int(n) for n in sys.stdin.readline().strip()])

visited = [[False for _ in range(M)] for _ in range(N)]
print(bfs(matrix, visited))