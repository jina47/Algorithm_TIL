from collections import deque as dq

# 입력
N, M = map(int, input().split())
lab = []
for _ in range(N):
    lab.append(list(map(int, input().split())))

# 바이러스 놓을 수 있는 칸 담는 virus
virus = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append([i, j])

# bfs
def bfs(lst):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 방문 여부 및 걸리는 시간 구하는 visited
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 1:
                visited[i][j] = -1
    
    que = dq(lst)
    # virus 놓는 곳 visited[x][y] = 1 처리 
    for [x, y] in lst:
        visited[x][y] = 1
    
    while que:
        x, y = que.popleft()
        # 상하좌우 탐색 후 빈칸이면 virus 퍼짐
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 방문하지 않았던 곳이면 인접한 곳으로 이동하는 데 1초 걸림
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append([nx, ny])
    
    # 모든 칸에 바이러스 퍼뜨리는데 걸리는 시간 max_time
    max_time = 0
    for i in range(N):
        for j in range(N):
            # 바이러스가 퍼뜨려지지 않은 곳이 있다면 'impossible' return
            if visited[i][j] == 0:
                return 'impossible'
            if visited[i][j] > max_time:
                max_time = visited[i][j]
    # 처음 바이러스를 놓는 시간을 1초라고 했으므로 파이러스가 퍼지는데 걸리는 시간은 max_time-1
    return max_time-1


# 바이러스 놓을 수 있는 경우 구하기            
answer = []
def search(temp, idx):
    # 바이러스를 M개 놓은 경우 bfs 실행 후 파이러스가 퍼지는데 걸리는 시간 answer에 담기
    if len(temp) == M:
        result = bfs(temp)
        if result != 'impossible':
            answer.append(result)
        return

    for new_id in range(idx+1, len(virus)):
        new_temp = temp + [virus[new_id]]
        search(new_temp, new_id)


# 바이러스를 놓을 수 있는 모든 경우를 찾고 최소 시간 구하기
for k in range(len(virus)-M+1):
    temp = [virus[k]]
    search(temp, k)


# answer이 빈 리스트라면 어떤 경우에도 바이러스를 퍼뜨릴 수 없으므로 -1 출력
if answer == []:
    print(-1)
# answer에 값이 있으면 최소값 출력
else:
    print(min(answer))