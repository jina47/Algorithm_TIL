# 입력
N, K = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())

# 바이러스가 있으면 [바이러스, 인덱스]를 담는 배열 idx 생성
idx = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            idx.append([matrix[i][j], i, j])
# 바이러스 번호가 작은 순서대로 정렬
idx.sort()

# 바이러스 번호 작은순서대로 상하좌우에 바이러스가 없으면 바이러스를 넣어줌
# S초가 되었거나 더 이상 넣어줄 바이러스가 없을 때 break
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
while cnt < S:
    temp = []
    for [v, r, c] in idx:
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = v
                    temp.append([v, nx, ny])
    if temp == []:
        break
    idx = temp
    cnt += 1

# 출력
print(matrix[X-1][Y-1])
