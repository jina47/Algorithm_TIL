R, C = map(int, input().split())
maps = []
for _ in range(R):
    maps.append([s for s in input().strip()])
# 50년 뒤의 지도
newmaps = [n[:] for n in maps]

row = []
col = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
for r in range(R):
    for c in range(C):
        # 땅의 주변 땅의 개수가 2개 이상이면 row에 r을 col에 c를 넣어줌
        if maps[r][c] == 'X':
            cnt = 0
            for i in range(4):
                nx = r+dx[i]
                ny = c+dy[i]
                if 0 <= nx < R and 0 <= ny < C and maps[nx][ny] == 'X':
                    cnt += 1
            if cnt >= 2:
                row.append(r)
                col.append(c)
            # 땅의 주변 땅의 개수가 2개 미만이라면 50년 후 지도에서 바다로 바꿔줌
            else:
                newmaps[r][c] = '.'
            
row.sort()
col.sort()
# row의 최소, 최대 범위에서 col의 최소, 최대 범위에서 newmaps 출력
for i in range(row[0], row[-1]+1):
    for j in range(col[0], col[-1]+1):
        print(newmaps[i][j], end= '')
    print()
