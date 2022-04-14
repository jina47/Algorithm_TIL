from collections import deque as dq

# 땅 크기 N, 인구 차이 기준 L, R
N, L, R = map(int, input().split())

# 주어진 나라의 인구 수
country = []
for r in range(N):
    temp = input().split()
    country.append([int(i) for i in temp])

# 인구 이동으로 변하는 인구 수를 표시할 땅
A = [c[:] for c in country]

# bfs이용
def bfs(x, y):
    global tf
    que = dq([[x, y]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 연합의 인구 수를 구하기 위한 리스트 lst
    lst = []
    visited[x][y] = cnt
    while que:
        [r, c] = que.popleft()
        if [r, c] not in lst:
            lst.append([r,c])
        # 상, 하, 좌, 우 칸이 범위를 벗어나지 않고 방문하지 않았어야 함
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] < cnt:
                # 인구 수 차이가 L과 R 사이라면 que에 append, 방문 표시
                if L <= abs(country[r][c] - country[nx][ny]) <= R:
                    que.append([nx, ny])
                    visited[nx][ny] = cnt
                    # 연합이 존재하면 tf = True
                    tf = True
    
    # 만약 연합이 존재하지 않으면 맨 처음 입력값에 대한 방문 값을 원래대로 돌려주고 return
    if tf == False:
        visited[x][y] -= 1
        return

    # 연합 존재 시 인구 이동 후 인구 수 구하기
    total = 0
    for [p, q] in lst:
        total += country[p][q]
    
    people = total //len(lst)
    for [p, q] in lst:
        A[p][q] = people
 

# 방문기록       
visited = [[0 for _ in range(N)] for _ in range(N)]

# 방문 안 한 기본값이 0이므로 cnt는 1부터 시작 (인구 이동 발생 일수)
cnt = 1
while True:
    tf = False
    # 모든 나라에 대해 탐색
    for r in range(N):
        for c in range(N):
            if visited[r][c] < cnt:
                bfs(r,c)
    
    # 모든 나라를 다 탐색하고 나서 country를 A로 갱신 
    # country 하나로만 이용하면 탐색 중간에 country 정보가 바뀜
    country = [a[:] for a in A]
    
    # 연합이 존재하면 그 다음날로 넘어가기 위해 cnt += 1
    if tf:
        cnt += 1
    # 만약 모든 나라에 대해 연합이 존재하지 않는다면 break
    else:
        break

# 애초에 1부터 시작했으므로 인구 이동 발생일 수는 cnt -1
print(cnt-1)