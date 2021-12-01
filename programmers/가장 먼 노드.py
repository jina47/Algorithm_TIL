from collections import deque as dq

def solution(n, vertex):
    # vertex의 노드들을 딕셔너리로 만들어주기
    edge = {}
    for w in vertex:
        [u, v] = w
        if u not in edge:
            edge[u] = [v]
        else:
            edge[u].append(v)
        if v not in edge:
            edge[v] = [u]
        else:
            edge[v].append(u)
    
    # 방문 여부 확인 위해 visited 생성
    visited = [0 for _ in range(n+1)]
    # start 노드인 1을 que에 넣어줌
    que = dq([1])
    # 1은 방문하고 시작하므로 visited[1] = 1
    visited[1] = 1
    # bfs 실행
    while que:
        node = que.popleft()
        for n in edge[node]:
            if visited[n] == 0:
                que.append(n)
                visited[n] = visited[node] + 1
    
    # visited의 최댓값이 몇 개인지 세어주고 return
    return visited.count(max(visited))
