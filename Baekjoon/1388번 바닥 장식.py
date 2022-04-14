# 세로 N, 가로 M
N, M = map(int, input().split())

# 방 바닥 장식
room = []
for _ in range(N):
    room.append([j for j in input()])

# dfs
def dfs(r, c):
    stack = [[r,c]]
    while stack:
        [x, y] = stack.pop()
        visited[x][y] = 1
        # '-'면 오른쪽도 '-'일 때 stack에 append
        if room[x][y] == '-':
            if y+1 < M and room[x][y+1] =='-' and visited[x][y+1] == 0:
                stack.append([x, y+1])
        # '|'면 아래쪽도 '|'일 때 stack에 append
        else:
            if x+1 < N and room[x+1][y] == '|' and visited[x+1][y] == 0:
                stack.append([x+1, y])

# 필요한 나무 판자 수 
cnt = 0
# 방문 처리
visited = [[0 for _ in range(M)] for _ in range(N)]
# 방문하지 않은 곳에서 cnt+=1 dfs 실행
for r in range(N):
    for c in range(M):
        if visited[r][c] == 0:
            cnt += 1
            dfs(r, c)

#출력
print(cnt)
