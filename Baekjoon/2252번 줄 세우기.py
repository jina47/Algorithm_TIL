from collections import deque as dq

# 위상정렬 이용
N, M = map(int, input().split())
height = [[] for _ in range(N+1)]
dg = [0 for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    height[A].append(B)
    dg[B] += 1

que = dq([])
for i in range(1, N+1):
    if dg[i] == 0:
        que.append(i)

line = []
while que:
    node = que.popleft()
    line.append(node)
    for adj in height[node]:
        dg[adj] -= 1
        if dg[adj] == 0:
            que.append(adj)
print(line)