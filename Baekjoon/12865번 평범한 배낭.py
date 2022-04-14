N, K = map(int, input().split())

weights = []
for _ in range(N):
    weights.append(list(map(int, input().split())))

bags = [[0 for _ in range(K+1)] for _ in range(N)]
for i in range(N):
    w = weights[i][0]
    v = weights[i][1]
    for j in range(1, K+1):
        if i == 0:
            if j >= w:
                bags[i][j] = v
        else:
            if j < w:
                bags[i][j] = bags[i-1][j]
            else:
                bags[i][j] = max(v+bags[i-1][j-w], bags[i-1][j])
print(bags[-1][-1])





