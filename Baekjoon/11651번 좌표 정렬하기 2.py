import sys

# 점의 개수 N
N = int(input())

# [x,y]를 담는 points
points = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append([x,y])

points.sort(key=lambda x: (x[1], x[0]))
for [x,y] in points:
    print(x, y)
