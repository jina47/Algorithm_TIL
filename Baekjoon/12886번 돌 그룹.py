from collections import deque as dq

A, B, C = map(int, input().split())

# A, B, C의 합이 3의 배수가 아니면 모든 그룹의 돌의 개수를 같게 만들 수 없음
if (A+B+C) % 3 != 0:
    print(0)
else:
    # A, B, C의 합은 항상 같으므로 두 개만 골라서 방문 처리 해주면 됨
    visited = [[0 for _ in range(1000)] for _ in range(1000)]
    [A, B, C] = sorted([A, B, C])
    que = dq([[A, B, C]])
    visited[A][B] = 1
    visited[B][C] = 1
    visited[A][C] = 1
    flag = False
    # bfs 실행
    while que:
        [x, y, z] = que.popleft()
        # 돌 개수를 같게 만든 경우 flag = True
        if x == y == z:
            flag = True
            break
        # 크기가 같지 않은 두 그룹을 골라 X+X, Y-X 연산 후 방문하지 않았으면 que에 추가
        if x != y:
            [nx, ny, nz] = sorted([x+x, y-x, z])
            if visited[nx][ny] == 0:
                que.append([nx, ny, nz])
                visited[nx][ny] = 1
        if x != z:
            [nx, ny, nz] = sorted([x+x, z-x, y])
            if visited[nx][ny] == 0:
                que.append([nx, ny, nz])
                visited[nx][ny] = 1
        if z != y:
            [nx, ny, nz] = sorted([y+y, z-y, x])
            if visited[nx][ny] == 0:
                que.append([nx, ny, nz])
                visited[nx][ny] = 1
    
    # flag가 True면 1 출력, False면 0 출력
    print(int(flag))