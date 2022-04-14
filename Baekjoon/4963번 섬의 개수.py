def dfs(maps, r, c):
    global w, h

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [0, 1, -1, 1, -1, 0, 1, -1]
    
    # maps[r][c]부터 시작해서 갈 수 있는 땅은 0의 값으로 바꿔줌
    stack = [[r, c]]
    while stack:
        [x, y] = stack.pop()
        maps[x][y] = 0
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == 1:
                stack.append([nx, ny])
    return maps

# 입력
while True:   
    w, h = map(int, input().split())
    # 0, 0 이 입력으로 들어오면 끝 
    if w == 0 and h == 0:
        break
    # 지도 생성
    maps = []
    for _ in range(h):
        maps.append([int(i) for i in input().split()])
    
    # 섬의 개수 dfs로 탐색
    cnt = 0
    for r in range(h):
        for c in range(w):
            if maps[r][c] == 1:
                maps = dfs(maps, r, c)
                cnt += 1
    print(cnt)
