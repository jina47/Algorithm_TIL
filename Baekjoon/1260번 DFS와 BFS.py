from collections import deque as dq

def bfs(graph, start):
    visited = []
    if start not in graph:
        visited.append(start)
        return visited

    que = dq([start])

    while que:
        node = que.popleft()
        if node not in visited:
            visited.append(node)
            for next in sorted(graph[node]):
                if next not in visited:
                    que.append(next)
    return visited

def dfs(graph, start):
    visited = []
    if start not in graph:
        visited.append(start)
        return visited

    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for next in sorted(graph[node], reverse=True):
                if next not in visited:
                    stack.append(next)
    return visited



N, M, start = map(int, input().split())

graph = {}
for _ in range(M):
    n1, n2 = map(int, input().split())
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)
    
    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)
    

print(' '.join(map(str, dfs(graph, start))))
print(' '.join(map(str, bfs(graph, start))))
