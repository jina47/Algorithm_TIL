N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input().split())))

for x in range(N):
    for y in range(M):
        # 첫 행에서는 왼쪽 옆의 항을 더해준다
        if x == 0 and y != 0:
            maze[x][y] += maze[x][y-1]
        # 두 번째 이상 행의 첫 번째 값은 바로 위의 값을 더해준다
        elif x != 0 and y == 0:
            maze[x][y] += maze[x-1][y]
        # 두 번째 이상 행에서 두 번째 이상의 값은 왼쪽과 위쪽의 최댓값을 더해준다
        elif x != 0 and y != 0:
            maze[x][y] += max(maze[x-1][y], maze[x][y-1])
# 마지막 값 출력
print(maze[-1][-1])
