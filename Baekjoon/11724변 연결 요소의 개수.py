import sys

# dfs 실행
def dfs(graph, visited, start):
    stack = [start]
    while stack:
        node = stack.pop()
        visited[node] = 1
        if node in graph:
            for nxt in graph[node]:
                if visited[nxt] == 0:
                    stack.append(nxt)
    return visited


# 입력
N, M = map(int, sys.stdin.readline().split())
graph = {}
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = [v]
    else:
        graph[u].append(v)
    if v not in graph:
        graph[v] = [u]
    else:
        graph[v].append(u)

# visited로 방문 여부 표시
visited = [0 for i in range(N+1)]
cnt = 0
for num in range(1, N+1):
    # visited[num] == 0 이면 dfs 실행 후 visited 갱신
    # cnt += 1
    if visited[num] == 0:
        cnt += 1
        visited = dfs(graph, visited, num)

# 연결 요소의 개수 cnt 출력
print(cnt)
