from collections import deque as dq

N = int(input())
graph = {}
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    if n1 != 1 and n2 != 1:
        if n1 not in graph:
            graph[n1] = [n2]
        else:
            graph[n1].append(n2)

        if n2 not in graph:
            graph[n2] = [n1]
        else:
            graph[n2].append(n1)
    else:
        if min(n1, n2) not in graph:
            graph[1] = [max(n1, n2)]
        else:
            graph[1].append(max(n1, n2))

# bfs 실행
# visited로 방문 여부 탐색
visited = [0 for _ in range(N+1)]
# parent에 부모 노드 저장
parent = [0 for _ in range(N+1)]
que = dq([1])
while que:
    node = que.popleft()
    visited[node] = 1
    if node in graph:
        for adjnode in graph[node]:
            if visited[adjnode] == 0:
                parent[adjnode] = node
                que.append(adjnode)
# 부모 노드 출력
for idx in range(2, N+1):
    print(parent[idx])
    
