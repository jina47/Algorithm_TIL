from collections import deque as dq

# bfs 이용
def bfs(graph):
    visited = []
    que = dq([1])
    while que:
        n = que.popleft()
        if n not in visited:
            visited.append(n)
            for s in graph[n]:
                if s not in visited:
                    que.append(s)
    return len(visited)



N = int(input())
M = int(input())

graph = {}
for _ in range(M):
    n1, n2 = map(int, input().split())
    if n1 not in graph:
        graph[n1] = [n2]
    else:
        graph[n1].append(n2)
    if n2 not in graph:
        graph[n2] = [n1]
    else:
        graph[n2].append(n1)


print(bfs(graph)-1)
