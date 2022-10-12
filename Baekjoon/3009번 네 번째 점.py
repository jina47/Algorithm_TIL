# 입력
points = []
for _ in range(3):
    points.append(list(map(int, input().split())))
points.sort()
if points[0][0] == points[1][0]:
    nx = points[2][0]
else:
    nx = points[0][0]
points.sort(key=lambda x : x[1])
if points[0][1] == points[1][1]:
    ny = points[2][1]
else:
    ny = points[0][1]
print(nx, ny)