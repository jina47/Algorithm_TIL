n = int(input())
pair = int(input())
neighbor = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(pair):
    c1, c2 = map(int, input().split())
    neighbor[c1].append(c2)
    neighbor[c2].append(c1)

que = [1]
visited[1] = 1
cnt = 0
while que:
    cur = que.pop(0)
    for n in neighbor[cur]:
        if visited[n] == 0:
            cnt += 1
            que.append(n)
            visited[n] = 1

print(cnt)
