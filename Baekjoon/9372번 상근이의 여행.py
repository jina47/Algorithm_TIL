from collections import deque as dq

def bfs(x):
    que = dq([x])
    visited[x] = 1
    cnt = 0
    while que:
        now = que.popleft()
        for adj in country[now]:
            # 새로 탐색하는 나라가 생기면 cnt += 1
            if visited[adj] == 0:
                que.append(adj)
                visited[adj] = 1
                cnt += 1
    return cnt
                

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    country = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        country[a].append(b)
        country[b].append(a)
    visited =[0 for _ in range(N+1)]
    answer = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            answer += bfs(i)
    print(answer)