from collections import deque as dq

# 입력
M, N = map(int, input().split())

rooms = []
for i in range(N):
    rooms.append([int(s) for s in input()])


# 부순 벽의 수를 담는 crashed
# 해당 지점까지 오는 데 부수는 벽의 최솟값을 담기 위해 초기값으로 10000을 넣어줌
crashed = [[10000 for _ in range(M)] for _ in range(N)]

# 시작점에서는 부수는 벽이 없음
crashed[0][0] = 0

# 상하좌우 판단
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# bfs 실행
que = dq([[0, 0]])
while que:
    x, y = que.popleft()

    # 인접한 상하좌우 판단
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상하좌우가 미로 방에 있을 때
        if 0 <= nx < N and 0 <= ny < M:
            # 만약 벽이라면 crashed[x][y]+1과 crashed[nx][ny]를 비교해서 더 작은 값을 담아줌
            if rooms[nx][ny] == 1 and crashed[nx][ny] > crashed[x][y]+1:
                crashed[nx][ny] = crashed[x][y] + 1
                que.append([nx, ny])
            # 만약 벽이 아닌 빈 방이라면 crashed[x][y]와 crashed[nx][ny]를 비교해서 더 작은 값을 담아줌
            elif rooms[nx][ny] == 0 and crashed[nx][ny] > crashed[x][y]:
                crashed[nx][ny] = crashed[x][y]
                que.append([nx, ny])


# bfs 실행환료 후 crashed[-1][-1] 값 출력
print(crashed[-1][-1])
