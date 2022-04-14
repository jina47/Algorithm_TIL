from collections import deque as dq

# 총 F층, 강호 S, 스타트링크 G
F, S, G, U, D = map(int, input().split())

# 방문 체크
visited = [0 for _ in range(F+1)]
visited[S] = 1

# bfs
def bfs():
    que = dq([S])
    while que:
        now = que.popleft()
        # 스타트링크에 도착시 break
        if now == G:
            break

        up = now + U
        down = now - D
        for next in [up, down]:
            # 위로 이동하거나 아래로 이동한 층이 1과 F사이의 값이어야 함
            if 1 <= next <= F and visited[next] == 0:
                que.append(next)
                visited[next] = visited[now] + 1
        
bfs()

# 만약 visited[G]가 0이라면 방문할 수 없는 것
if visited[G] != 0:
    print(visited[G]-1)
else:
    print("use the stairs")
