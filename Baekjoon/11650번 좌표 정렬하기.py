import sys

# 점의 개수 N
N = int(input())

# x, y 좌표 리스트에 담기
points = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append([x,y])

# x증가하는 순서대로 정렬, x같으면 y증가하는 순서대로 정렬
points.sort(key=lambda x:(x[0], x[1]))

# 출력
for [x,y] in points:
    print(x, y)