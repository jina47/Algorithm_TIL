import sys
import heapq

# 다익스트라 알고리즘
def dijkstra(graph, start, end):
    global N
    # 최소 비용을 구하기 위한 costs 생성
    costs = {node: float('inf') for node in range(1, N+1)}
    costs[start] = 0
    que = []
    # 우선순위를 비용으로 정하기 위해 que에 [0, start] append
    heapq.heappush(que, [0, start])
    while que:
        [cost, city] = heapq.heappop(que)

        # 저장되어있는 최소비용보다 현재 비용이 더 작을 때만 수행
        if costs[city] >= cost:
            # graph[city]가 있을 때
            if city in graph and graph[city]:
                for adjcity, adjcost in graph[city].items():
                    newcost = adjcost + cost
                    # 인접한 도시까지 가는 데 필요한 새로 구한 비용과 이미 저장되어있는 인접한 도시까지의 비용 비교
                    if newcost < costs[adjcity]:
                        costs[adjcity] = newcost
                        que.append([newcost, adjcity])
    return costs[end]

# 입력
N = int(input())
M = int(input())
# 딕셔너리 타입으로 graph 저장
graph = {}
for _ in range(M):
    s, e, c = map(int, sys.stdin.readline().split())
    if s not in graph:
        graph[s] = {e : c}
    else:
        if e not in graph[s]:
            graph[s][e] = c
        else:
            if graph[s][e] > c:
                graph[s][e] = c
# 시작점, 끝점 이용해서 dijkstra 알고리즘 수행
start, end = map(int, sys.stdin.readline().split())
print(dijkstra(graph, start, end))
