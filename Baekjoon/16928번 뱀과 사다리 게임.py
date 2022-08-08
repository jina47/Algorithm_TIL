from collections import deque as dq
# 입력
N, M = map(int, input().split())
# 사다리, 뱀 딕셔너리로 만들기
ladder = {}
snake = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v
# 주사위 최소 횟수 담는 리스트
dice = [0 for _ in range(101)]

# bfs 실행
que = dq([1])
while que:
    x = que.popleft()

    # 100번째 칸에 도착했을 때 필요한 주사위 횟수 출력
    if x == 100:
        print(dice[x])
        break

    # 주사위로 나올 수 있는 수 1~6
    for dx in range(1, 7):
        nx = x+dx
        # 주사위를 던져 나온 수를 더한 번호 nx (100을 넘을 수 없음)
        if nx <= 100:
            # 만약 사다리가 있는 칸이라면 올라감
            if nx in ladder.keys():
                nx = ladder[nx]
            # 만약 뱀이 있는 칸이라면 내려감
            elif nx in snake.keys():
                nx = snake[nx]
            # 새로 정해진 nx가 방문한 적이 없다면 que에 append
            if  dice[nx] == 0:
                que.append(nx)
                # x에서 주사위를 한 번 더 굴려주어야 nx에 도달
                dice[nx] = dice[x] + 1

