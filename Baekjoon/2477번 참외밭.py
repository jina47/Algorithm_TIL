K = int(input())
points = []
for _ in range(6):
    points.append(list(map(int, input().split())))
visited = [0 for _ in range(5)]
sh, sw = 0, 0
for i, [d, l] in enumerate(points):
    if visited[d] == 0:
        visited[d] = l
    else:
        if d == 1 or d == 2:
            sw = d
        if d == 3 or d == 4:
            sh = d
        if visited[d] < l:
            visited[d] = l
h = max(visited[3], visited[4])
w = max(visited[1], visited[2])

for i, [d, l] in enumerate(points):
    if i == 0:
        if d == 1 or d == 2:
            if points[5][1] != h and points[1][1] != h:
                sw = l
        elif d == 3 or d == 4:
            if points[5][1] != w and points[1][1] != w:
                sh = l
    elif i == 5:
        if d == 1 or d == 2:
            if points[0][1] != h and points[4][1] != h:
                sw = l
        elif d == 3 or d == 4:
            if points[0][1] != w and points[4][1] != w:
                sh = l
    else:
        if d == 1 or d == 2:
            if points[i-1][1] != h and points[i+1][1] != h:
                sw = l
        elif d == 3 or d == 4:
            if points[i-1][1] != w and points[i+1][1] != w:
                sh = l
       
print((h*w - sh*sw)*K)


