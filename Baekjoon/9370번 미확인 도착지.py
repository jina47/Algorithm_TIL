import sys
import heapq

def dijkstra(graph, n, start, goal):
    distances = {node: float('inf') for node in range(1, n+1)}
    distances[start] = 0
    que = []
    heapq.heappush(que, [0, start])
    cnt = 0
    while que:
        [distance, node] = heapq.heappop(que)
        if node == goal:
            break
        cnt += 1
        if distances[node] >= distance and node in graph:
            for [adn, add] in graph[node]:
                nd = add + distance
                if nd < distances[adn]:
                    distances[adn] = nd
                    que.append([nd, adn])
    return [distances[goal], cnt]
 

T = int(input())
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    graph = {}
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        if a not in graph:
            graph[a] = [[b, d]]
        else:
            graph[a].append([b, d])
        if b not in graph:
            graph[b] = [[a, d]]
        else:
            graph[b].append([a, d])
    
    path = []
    for _ in range(t):
        end = int(sys.stdin.readline())
        p1 = dijkstra(graph, n, s, g)[0] + dijkstra(graph, n, g, h)[0] + dijkstra(graph, n, h, end)[0]
        e1 = dijkstra(graph, n, s, g)[1] + dijkstra(graph, n, g, h)[1] + dijkstra(graph, n, h, end)[1]
        p2 = dijkstra(graph, n, s, h)[0] + dijkstra(graph, n, h, g)[0] + dijkstra(graph, n, g, end)[0]
        e2 = dijkstra(graph, n, s, h)[1] + dijkstra(graph, n, h, g)[1] + dijkstra(graph, n, g, end)[1]
        print(p1, p2, e1, e2)
        if p1 != float('inf') or p2 != float('inf'):
            path.append(end)
    print(' '.join(map(str, sorted(path))))
        