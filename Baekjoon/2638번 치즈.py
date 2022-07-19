N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# 치즈가 다 녹는 데 걸리는 시간
cnt = 1
while True:
    # new_board는 한 시간 후 치즈가 녹은 후의 board판 모습
    # 시간마다 new_board, visited 갱신
    new_board = [b[:] for b in board]    
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    # dfs로 방문처리
    stack = [[0, 0]]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while stack:
        [x, y] = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 상하좌우 탐색
            if 0 <= nx < N and 0 <= ny < M:
                # 0이면 치즈 외곽이므로 방문처리 & stack에 append
                if board[nx][ny] == 0 and visited[nx][ny] == 0:
                    stack.append([nx, ny])
                    visited[nx][ny] = 1
                # 1이고 new_board[nx][ny] != 0이면 다음에 녹을 치즈인지 확인
                elif board[nx][ny] == 1 and new_board[nx][ny] != 0:
                    # 외부 공기와 한 번 접촉할 때마다 -1
                    visited[nx][ny] -= 1
                    # 외부 공기와 2변 이상이 접촉하면 다음에 녹는 치즈
                    if visited[nx][ny] <= -2:
                        new_board[nx][ny] = 0

    # new_board가 모두 0이 되면 치즈가 모두 녹은 것이므로 break
    if max(map(max, new_board)) == 0:
        break
    else:
        board = new_board
        cnt += 1

print(cnt)