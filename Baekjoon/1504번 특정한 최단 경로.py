import sys
import heapq

def dijkstra(graph, start, end):
    global N
    distances = {node:float('inf') for node in range(1, N+1)}
    distances[start] = 0
    que = []
    heapq.heappush(que, [0,start])
    while que:
        [distance, node] = heapq.heappop(que)
        if distances[node] >= distance and node in graph:
            for an, ad in graph[node].items():
                nd = ad+distance
                if nd < distances[an]:
                    heapq.heappush(que, [nd, an])
                    distances[an] = nd
    return distances[end]


# 입력
N, E = map(int, sys.stdin.readline().split())
graph = {}
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    if a not in graph:
        graph[a] = {b:c}
    else:
        if b not in graph[a]:
            graph[a][b] = c
    if b not in graph:
        graph[b] = {a:c}
    else:
        if a not in graph[b]:
            graph[b][a] = c
v1, v2 = map(int, sys.stdin.readline().split())

# 출력
p1 = dijkstra(graph, 1, v1) + dijkstra(graph, v1, v2) + dijkstra(graph, v2, N)
p2 = dijkstra(graph, 1, v2) + dijkstra(graph, v2, v1) + dijkstra(graph, v1, N)

if p1 == float('inf') and p2 == float('inf'):
    print(-1)
else:
    print(min(p1, p2))