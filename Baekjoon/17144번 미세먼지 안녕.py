import sys

# 입력
R, C, T = map(int, input().split())
room = [[] for _ in range(R)]
cleaner = []
for i in range(R):
    for idx, p in enumerate(sys.stdin.readline().split()):
        room[i].append(int(p))
        if int(p) == -1:
            cleaner.append([i, idx])

# 확산 & 정화
def spread(room):
    # 미세먼지 확산
    new_room = [[0 for _ in range(C)] for _ in range(R)]
    for [nr, nc] in cleaner:
        new_room[nr][nc] = -1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for r in range(R):
        for c in range(C):
            if room[r][c] not in [-1, 0]:
                amount = room[r][c] // 5
                cnt = 0
                for i in range(4):
                    nx = r + dx[i]
                    ny = c + dy[i]
                    if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:
                        new_room[nx][ny] += amount
                        cnt += 1
                new_room[r][c] += room[r][c] - cnt * amount 
    room = new_room
    
    # 공기청정기 정화
    new_room = [[0 for _ in range(C)] for _ in range(R)]
    for [nr, nc] in cleaner:
        new_room[nr][nc] = -1
    
    for r in range(R):
        for c in range(C):
            if room[r][c] not in [-1, 0]:
                if r not in [0, cleaner[0][0], cleaner[1][0], R-1] and c not in [0, C-1]:
                    new_room[r][c] = room[r][c]
                # 반시계
                elif 0 <= r < cleaner[0][0]-1 and c == 0:
                    new_room[r+1][c] = room[r][c]
                elif r == cleaner[0][0] and 0 < c < C-1:
                    new_room[r][c+1] = room[r][c]
                elif 0 < r <= cleaner[0][0] and c == C-1:
                    new_room[r-1][c] = room[r][c]
                elif r == 0 and 0 < c < C:
                    new_room[r][c-1] = room[r][c]
                # 시계
                elif cleaner[1][0]+1 < r < R and c == 0:
                    new_room[r-1][c] = room[r][c]
                elif r == cleaner[1][0] and 0 < c < C-1:
                    new_room[r][c+1] = room[r][c]
                elif cleaner[1][0] <= r < R-1 and c == C-1:
                    new_room[r+1][c] = room[r][c]
                elif r == R-1 and 0 < c < C:
                    new_room[r][c-1] = room[r][c]
    return new_room


# T초까지 확산, 정화 반복
time = 0                
while time < T:
    room = spread(room)
    time += 1 

# 출력
answer = 0
for idx in range(R):
    answer += sum(room[idx])
print(answer+2)