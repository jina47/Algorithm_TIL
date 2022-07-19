import sys

H, W = map(int, sys.stdin.readline().strip().split())
board = []
for _ in range(H):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

# 치즈가 다 녹는 데 걸리는 시간
cnt = 1
while True:
    # 시간마다 new_board, visited 갱신
    new_board = [b[:] for b in board]    
    visited = [[0 for _ in range(W)] for _ in range(H)]
    # 치즈 외곽 dfs로 방문처리
    stack = [[0, 0]]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while stack:
        [x, y] = stack.pop()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 상하좌우 중 방문 안 한 곳
            if 0 <= nx < H and 0 <= ny < W and visited[nx][ny] == 0:
                # 0이면 치즈 외곽이므로 방문처리해주기 위해 stack에 append
                if board[nx][ny] == 0:
                    stack.append([nx, ny])
                # 1이면 다음 시간에 녹을 치즈 부분이므로 new_board[nx][ny] = 0
                elif board[nx][ny] == 1:
                    new_board[nx][ny] = 0
    # new_board가 모두 0이 되면 치즈가 모두 녹은 것이므로 break
    if max(map(max, new_board)) == 0:
        break
    else:
        board = new_board
        cnt += 1

# 치즈가 다 녹는데 걸리는 시간 출력
print(cnt)
# 마지막으로 다 녹기 전 치즈 조각 개수
answer = 0
for x in range(H):
    for y in range(W):
        if board[x][y] == 1:
            answer += 1
print(answer)

