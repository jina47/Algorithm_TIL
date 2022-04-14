n = int(input())
m = int(input())
# 최소 비용을 구하기 위해 애초의 값은 inf로 설정
cost = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if cost[a][b] == 0:
        cost[a][b] = c
    elif cost[a][b] != 0 and cost[a][b] > c:
        cost[a][b] = c
# 플로이드 와샬 알고리즘
# k는 경유지이고 자기 자신으로 가는 비용은 0
for k in range(1, n+1):
    cost[k][k] = 0
    for start in range(1, n+1):
        for end in range(1, n+1):
            # 원래의 비용과 k를 경유해서 도착하는 경우의 비용을 비교해서 최솟값으로 설정
            cost[start][end] = min(cost[start][end], cost[start][k] + cost[k][end])

for row in range(1, n+1):
    for col in range(1, n+1):
        if cost[row][col] == float('inf'):
            cost[row][col] = 0
    print(' '.join(map(str, cost[row][1:])))

    