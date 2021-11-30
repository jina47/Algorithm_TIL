def solution(n, computers):
    graph = {}
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                if i not in graph:
                    graph[i] = [[i, j]]
                else:
                    graph[i].append([i,j])
    
    # dfs로 네트워크 수 찾기
    visited = [0 for i in range(n)]
    answer = 0
    for i in range(n):
        if visited[i] == 0:
            stack = [[i, i]]
            while stack:
                [u, v] = stack.pop()
                if visited[v] == 0:
                    visited[v] = 1
                    if v in graph:
                        for [nu, nv] in graph[v]:
                            if visited[nv] == 0:
                                stack.append([nu, nv])
            answer += 1
    return answer
