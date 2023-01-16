t = int(input()) # 테스트 케이스
for _ in range(t):
    n = int(input()) # 편의점 개수
    store = []
    for i in range(n+2):
        if i == 0: # 집 좌표
            sx, sy = map(int, input().split())
        elif i == n+1: # 페스티벌 좌표
            gx, gy = map(int, input().split())
        else: # 편의점 좌표
            store.append(list(map(int, input().split())))
    
    # dfs
    visited = [0 for _ in range(len(store))]
    stack = [-1]
    happy = False
    while stack:
        # 현재 위치 x, y
        num = stack.pop()
        if num == -1:
            x, y = sx, sy
        else:
            # 이동한 편의점 방문 처리
            [x, y] = store[num]
            visited[num] = 1
        
        # 현재 위치에서 목적지까지 거리가 1000미터 이내면 도착 가능
        if abs(x-gx) + abs(y-gy) <= 50*20:
            happy = True
            break
        
        # 목적지까지 갈 수 없으면 이동할 수 있는 편의점 찾기
        for i in range(len(store)):
            if visited[i] == 0:
                [nx, ny] = store[i]
                if abs(x-nx) + abs(y-ny) <= 50*20:
                    stack.append(i)
    
    # 목적지까지 도착 가능하면 happy, 불가능하면 sad 출력
    if happy == True:
        print('happy')
    else:
        print('sad')

        