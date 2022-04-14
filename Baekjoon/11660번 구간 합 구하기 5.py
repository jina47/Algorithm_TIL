import sys

N, M = map(int, sys.stdin.readline().split())
matrix = [[0 for _ in range(N+1)]]
for _ in range(N):
    matrix.append([0] + list(map(int, sys.stdin.readline().split())))

# dp 구현
for row in range(1, N+1):
    for col in range(1, N+1):
        matrix[row][col] += matrix[row-1][col] + matrix[row][col-1] - matrix[row-1][col-1]

# 원하는 값 출력
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(matrix[x2][y2]-matrix[x2][y1-1]-matrix[x1-1][y2]+matrix[x1-1][y1-1])