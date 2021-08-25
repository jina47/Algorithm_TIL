def solution(m, n, puddles):
    x = 1
    y = 1
    road = [[0 for j in range(m+1)] for i in range(n+1)]
    road[1][1] = 1
    while x != n+1:
        y += 1
        if [y,x] not in puddles:
            road[x][y] = road[x-1][y] + road[x][y-1]
        if y == m:
            x += 1
            y = 0
    return road[-1][-1] % 1000000007