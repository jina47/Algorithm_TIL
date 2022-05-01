import sys

N, M = map(int, input().split())
ocean = []
for _ in range(N):
    ocean.append(list(map(int, sys.stdin.readline().split())))

time = 0
while True:
    # 녹고 난 후를 기록할 new_ocean
    new_ocean = [[0 for _ in range(M)] for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for x in range(N):
        for y in range(M):
            # 빙산이 있는 경우
            if ocean[x][y] != 0:
                # 빙산이 녹아 줄어들 높이 cnt
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and ocean[nx][ny] == 0:
                        cnt += 1
                # 높이는 0보다 더 줄어들지 않음
                if ocean[x][y] >= cnt:
                    new_ocean[x][y] = ocean[x][y] - cnt
    
    # 빙산이 녹고 난 후 ocean 갱신
    ocean = new_ocean

    # 덩어리 확인 dfs
    visited = [[0 for _ in range(M)] for _ in range(N)]
    # 덩어리 개수 cnt_dfs
    cnt_dfs = 0
    for R in range(N):
        for C in range(M):
            # 빙산이 존재하고 방문한 적이 없으면 dfs 실행
            if ocean[R][C] != 0 and visited[R][C] == 0:
                cnt_dfs += 1
                stack = [[R, C]]
                visited[R][C] = cnt_dfs
                while stack:
                    [r, c] = stack.pop()
                    for id in range(4):
                        nx = r + dx[id]
                        ny = c + dy[id]
                        if 0 <= nx < N and 0 <= ny < M and ocean[nx][ny] != 0 and visited[nx][ny] == 0:
                            stack.append([nx, ny])
                            visited[nx][ny] = visited[r][c] 
    # 걸린 시간
    time += 1

    # 두 덩어리 이상으로 분리되면 break
    if max(map(max, visited)) >= 2:
        break
    
    # 분리가 되지 않았는데 빙산이 다 녹았을 경우 time=0으로 설정 후 break
    if max(map(max, ocean)) <= 0:
        time = 0
        break
                
# time 출력
print(time)

