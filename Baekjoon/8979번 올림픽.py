import sys

N, K = map(int, sys.stdin.readline().split())
medal = []
for _ in range(N):
    medal.append(list(map(int, sys.stdin.readline().split())))

medal.sort(key=lambda x : (-x[1], -x[2], -x[3]))
rank = [0 for _ in range(N)]
rank[0] = 1
for i in range(1, N):
    if medal[i-1][1:] == medal[i][1:]:
        rank[i] = rank[i-1]
    else:
        rank[i] = i+1

for j in range(N):
    if medal[j][0] == K:
        print(rank[j])