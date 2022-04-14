from collections import deque as dq

T = int(input())
for _ in range(T):
    l = int(input())
    row, col = map(int, input().split())
    gx, gy = map(int, input().split())
    matrix = [[0 for _ in range(l)] for _ in range(l)]
    
    matrix[row][col] = 1
    dx = [-2,-2,-1,-1,1,1,2,2]
    dy = [-1,1,-2,2,-2,2,-1,1]
    que = dq([[row, col]])
    
    visited = [[0 for _ in range(l)] for _ in range(l)]
    visited[row][col] = 1

    while que:
        [x, y] = que.popleft()
        if x == gx and y == gy:
            print(visited[gx][gy] -1)
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if visited[nx][ny] == 0:
                    que.append([nx, ny])
                    visited[nx][ny] = visited[x][y] +1



