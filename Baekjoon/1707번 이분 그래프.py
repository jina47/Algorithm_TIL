from collections import deque as dq
import sys


K = int(input())
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())

    graph = {}
    for i in range(E):
        u, v = map(int, sys.stdin.readline().split())
        if u not in graph:
            graph[u] = [v]
        else:
            graph[u].append(v)
        if v not in graph:
            graph[v] = [u]
        else:
            graph[v].append(u)

    visited = [0 for _ in range(V+1)]
   
    temp = True
    que = dq([1])
    while que:
        n1 = que.popleft()
        if visited[n1] <= 0:
            visited[n1] = -1
            if n1 in graph:
                l, r = 0, 0
                for n2 in graph[n1]:
                    if visited[n2] == 0:
                        visited[n2] = -1
                        que.append(n2)
                    elif visited[n2] > 0:
                        if l == 1 and r == 1:
                            break
                        if visited[n2] == 1:
                            l = 1
                        if visited[n2] == 2:
                            r = 1

                if l == 0 and r == 0:
                    visited[n1] = 1
                elif l == 1 and r == 0:
                    visited[n1] = 2
                elif l == 0 and r == 1:
                    visited[n1] = 1
                elif l == 1 and r == 1:
                    temp = False
                    break

            if not que:
                for i in range(1, V+1):
                    if visited[i] == 0:
                        que.append(i)
                        break
    
    if temp:
        print('YES')
    else:
        print('NO')
        




