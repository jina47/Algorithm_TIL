import sys

def solution(x, y, N):
    global m, z, o
    start = matrix[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if matrix[i][j] != start:
                solution(x, y, N//3)
                solution(x, y+N//3, N//3)
                solution(x, y+(N//3*2), N//3)
                solution(x+N//3, y, N//3)
                solution(x+N//3, y+N//3, N//3)
                solution(x+N//3, y+(N//3*2), N//3)
                solution(x+(N//3*2), y, N//3)
                solution(x+(N//3*2), y+N//3, N//3)
                solution(x+(N//3*2), y+(N//3*2), N//3)
                return
    
    if start == -1:
        m += 1
    elif start == 0:
        z += 1
    else:
        o += 1

# 입력
N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
m, z, o = 0, 0, 0
solution(0, 0, N)
print(m)
print(z)
print(o)