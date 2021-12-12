N, M = map(int, input().split())
x, y, d = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
# 상, 우, 하, 좌 기준으로 dx, dy 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
while True:
    # 벽이 아니면 -1로 지정해주기
    if matrix[x][y] != 1:
        matrix[x][y] = -1
        # 북쪽 방향인 경우 왼쪽부터 탐색
        if d == 0:
            turn = [3, 2, 1, 0]
        # 동쪽 방향인 경우 위쪽부터 탐색
        elif d == 1:
            turn = [0, 3, 2, 1]
        # 남쪽 방향인 경우 오른쪽부터 탐색
        elif d == 2:
            turn = [1, 0, 3, 2]
        # 서쪽 방향인 경우 아래쪽부터 탐색
        elif d == 3:
            turn = [2, 1, 0, 3]
        # 탐색해서 청소할 수 있으면 그 칸으로 이동
        for i in turn:
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
                x, y = nx, ny
                d = i
                break
        # 탐색했는데 청소할 수 있는 칸이 없을 때 현재 방향 기준으로 후진
        else:
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1 
    # 벽이 있는 칸으로 후진했다는 것은 탐색을 다 했는데 청소할 수 있는 칸이 더 이상 없거나 벽인 경우였으므로 작동 멈춤 break
    else:
        break

# 청소를 한 칸은 -1로 지정해줬으므로 matrix 탐색해서 청소한 칸 개수 찾기
cnt = 0
for j in range(N):
    for k in range(M):
        if matrix[j][k] == -1:
            cnt += 1

print(cnt)
