# dfs 실행
def dfs(visited, rgb, start, cnt):
    [r, c] = start
    visited[r][c] = cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = [[r, c]]
    while stack:
        [x, y] = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if rgb[nx][ny] == rgb[r][c] and visited[nx][ny] == 0:
                    visited[nx][ny] = cnt
                    stack.append([nx, ny])
    return visited

# 입력
N = int(input())
# picture은 일반인, rgb는 적록색약 기준 그림
picture = [[] for _ in range(N)]
rgb = [[] for _ in range(N)]
for idx in range(N):
    for s in input().strip():
        picture[idx].append(s)
        if s == 'G':
            rgb[idx].append('R')
        else:
            rgb[idx].append(s)
# 방문여부를 일반인은 vp, 적록색약은 vr로 탐색
vp = [[0 for _ in range(N)] for _ in range(N)]
vr = [[0 for _ in range(N)] for _ in range(N)]
# 구역을 일반인은 cp, 적록색약은 cr로 구분
cp = 0
cr = 0
# dfs로 구역 탐색
for i in range(N):
    for j in range(N):
        if vp[i][j] == 0:
            cp += 1
            vp = dfs(vp, picture, [i, j], cp)
        if vr[i][j] == 0:
            cr += 1
            vr = dfs(vr, rgb, [i, j], cr)
# 출력
answer = []
answer.append(max(map(max, vp)))
answer.append(max(map(max, vr)))
print(' '.join(map(str, answer)))
