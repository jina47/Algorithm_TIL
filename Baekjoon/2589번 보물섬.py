from collections import deque as dq

# 보물지도 세로 R, 가로 C
R, C = map(int, input().split())

# 보물지도 maps
maps = []
for _ in range(R):
    maps.append([s for s in input()])

# 보물 사이 최단거리 이동하는 시간
hour = 0

# bfs 이용
def bfs(r, c):
    # 방문 체크 visited
    visited = [[0 for _ in range(C)] for _ in range(R)]
    visited[r][c] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    que = dq([[r,c]])
    while que:
        [x, y] = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                # 방문하지 않은 육지라면 que에 append
                if visited[nx][ny] == 0 and maps[nx][ny] == 'L':
                    visited[nx][ny] = visited[x][y] + 1
                    que.append([nx, ny])
    
    # visited 중 최댓값 -1가 걸린 시간
    return max(map(max, visited)) -1


for r in range(R):
    for c in range(C):
        if maps[r][c] == 'L':
            # bfs(r,c)와 hour중의 최댓값 저장
            hour = max(bfs(r,c), hour)

#  출력
print(hour)
