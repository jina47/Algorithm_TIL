from collections import deque as dq

# 잡아먹을 수 있는 물고기 확인 함수
def find_fish(matrix, shark):
    for i in range(N):
        for j in range(N):
            # 잡아먹을 수 있는 물고기가 있는 경우 True
            if 0 < matrix[i][j] < shark:
                return True
    # 잡아먹을 수 있는 물고기가 없는 경우 False
    return False

# bfs 방식으로 아기상어가 물고기를 잡아먹음
def bfs(matrix, x, y):
    # 구하고 싶은 시간 second
    second = 0
    # 상어의 크기 shark
    shark = 2
    # 잡아먹는 물고기 수 eat
    eat = 0

    # 방문여부 확인을 위한 visited
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[x][y] = 1

    # bfs를 이용하기 위한 deque 설정
    que = dq([[x, y, 0]])
    # 상, 좌, 우, 하 순서로 탐색하기 위해 설정
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    while que:
        [x, y, time] = que.popleft()
        # matrix[x][y]값이 0이거나 shark와 같으면 주변을 탐색해서 que에 넣어줌
        if matrix[x][y] == 0 or matrix[x][y] == shark:
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                # 방문하지 않은 곳이면서 shark 이하의 값을 가지면 que에 append
                if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] <= shark and visited[nx][ny] == 0:
                    que.append([nx, ny, time+1])
                    visited[nx][ny] = 1
                    # 만약 물고기가 있는 경우에는 더 탐색하지 않고 break
                    if 0 < matrix[nx][ny] < shark:
                        break 
        
        # 물고기를 잡아먹는 경우
        elif 0 < matrix[x][y] < shark:
            # queue라는 리스트로 time이 같은 값 중 가장 인덱스가 작은 값을 탐색
            # 현재 값은 que에서 pop되어있으므로 queue에 넣어준 후 탐색
            queue = [[x, y, time]] + list(que)
            queue.sort()
            for q in queue:
                # 원하는 값을 찾으면 x, y, time을 새롭게 지정 후 break
                if 0 < matrix[q[0]][q[1]] < shark and time == q[2]:
                    x, y = q[0], q[1]
                    break
            # 상어가 물고기를 먹었으므로 eat에 1을 더해줌
            eat += 1
            # 물고기를 먹었으므로 해당 값은 0이 되어야 함
            matrix[x][y] = 0
            # 지나온 시간은 time만큼이므로 second에 더해줌
            second += time

            # 상어가 먹은 물고기의 수가 상어의 크기만큼이면 상어는 몸집이 커짐
            if eat == shark:
                shark += 1
                eat = 0
            # eat, que, visited 갱신
            que = dq([[x, y, 0]])
            visited = [[0 for _ in range(N)] for _ in range(N)]

            # 만약 더 이상 물고기를 먹을 수 없다면 while문에서 break
            if find_fish(matrix, shark) == False:
                break
    # 원하는 값 second 출력    
    print(second)

# 입력
N = int(input())
matrix = [[] for _ in range(N)]
cnt = 0
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        matrix[i].append(temp[j])
        if temp[j] == 0:
            cnt += 1
        # 아기 상어의 처음 위치 x, y
        elif temp[j] == 9:
            x, y = i, j

# 상어가 있는 위치는 물고기가 없으므로 0으로 지정
matrix[x][y] = 0

# 물고기가 없으면 0 출력
if cnt == N*N-1:
    print(0)
# 물고기가 있으면 잡아먹을 수 있는 시간 계산
else:
    bfs(matrix, x, y)
