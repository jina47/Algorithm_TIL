from collections import deque as dq

def solution(maps):
    # maps는 n*m 2차원 배열
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # bfs 이용하여 최단 거리 탐색
    que = dq([[0, 0]])
    while que:
        [x, y] = que.popleft()
        # x와 y가 원하는 값이면 return
        if x == n-1 and y == m-1:
            return maps[x][y]
        # 아직 목적지에 도달하지 않았다면 동,서,남,북이 벽이 아닌지 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 아니라면 maps[x][y]에 1을 더해준 값으로 지정
                if maps[nx][ny] == 1:
                    que.append([nx, ny])
                    maps[nx][ny] = maps[x][y] + 1
    
    # 목적지에 도달하지 못하면 -1 return
    return -1
