# 입력
N, M, x, y, K = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))
command = list(map(int, input().split()))
# 주사위 전개도 따라 verti = [뒷면, 윗면, 앞면, 아랫면], horizon = [왼쪽, 윗면, 오른쪽]
verti = [0, 0, 0, 0]
horizon = [0, 0, 0]

for num in command:
    # 동쪽으로 이동
    if num == 1 and y+1 < M:
        y += 1
        temp = [verti[1], verti[3]]
        verti[1] = horizon[0]
        verti[3] = horizon[2]
        horizon[0], horizon[1], horizon[2] = temp[1], verti[1], temp[0]
        print(verti[1])
        if maps[x][y] == 0:
            maps[x][y] = verti[3]
        else:
            verti[3] = maps[x][y]
            maps[x][y] = 0
    # 서쪽으로 이동
    elif num == 2 and y-1 >= 0:
        y -= 1
        temp = [verti[1], verti[3]]
        verti[1] = horizon[2]
        verti[3] = horizon[0]
        horizon[0], horizon[1], horizon[2] = temp[0], verti[1], temp[1]
        print(verti[1])
        if maps[x][y] == 0:
            maps[x][y] = verti[3]
        else:
            verti[3] = maps[x][y]
            maps[x][y] = 0
    # 북쪽으로 이동
    elif num == 3 and x-1 >= 0:
        x -= 1
        verti = verti[1:] + [verti[0]]
        horizon[1] = verti[1]
        print(verti[1])
        if maps[x][y] == 0:
            maps[x][y] = verti[3]
        else:
            verti[3] = maps[x][y] 
            maps[x][y] = 0
    # 남쪽으로 이동  
    elif num == 4 and x+1 < N:
        x += 1
        verti = [verti[3]] + verti[:3]
        horizon[1] = verti[1]
        print(verti[1])
        if maps[x][y] == 0:
            maps[x][y] = verti[3]
        else:
            verti[3] = maps[x][y]
            maps[x][y] = 0