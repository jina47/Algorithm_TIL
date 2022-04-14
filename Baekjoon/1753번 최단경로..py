import sys
import heapq

def dijkstra(graph, K, V):
    # distances의 각 정점에 무한대의 거리 설정
    distances = {n : float('INF') for n in range(1, V+1)}
    # start 지점인 K의 값은 거리가 0
    distances[K] = 0
    # heapq을 이용하여 저장된 거리 순서대로 정렬
    que = []
    heapq.heappush(que, [0, K])
    while que:
        [dist, node] = heapq.heappop(que)
        # 새로 탐색해줄 거리가 node에 저장된 거리보다 작거나 같을 때 인접 node 탐색
        # node가 그래프에 있는 key값이어야 함
        if distances[node] >= dist and node in graph:
            # graph[node]의 인접노드와 인접거리로 for문 탐색
            for adnode, addist in graph[node].items():
                # 인접거리와 dist의 합이 adnode에 저장된 거리보다 작을 때 갱신
                nw = addist + dist
                if nw < distances[adnode]:
                    distances[adnode] = nw
                    # [nw, adnode]를 que에 넣어줌
                    heapq.heappush(que, [nw, adnode])

    return distances
                


# 입력
V, E = map(int, input().split())
K = int(input())
graph = {}
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = {v: w}
    else:
        if v not in graph[u]:
            graph[u][v] = w
        else:
            if graph[u][v] > w:
                graph[u][v] = w


# 다익스트라 알고리즘 수행 후 출력
d = dijkstra(graph, K, V)
# 경로가 없는 경우 무한대로 설정되어 있을 것
for k, v in d.items():
    if v == float('INF'):
        print('INF')
    else:
        print(v)        

