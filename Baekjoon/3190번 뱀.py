from collections import deque as dq

N = int(input())
K = int(input())

matrix = [[0 for _ in range(N)] for _ in range(N)]
# 사과가 있으면 1로 표현
for _ in range(K):
    r, c = map(int, input().split())
    matrix[r-1][c-1] = 1

# 방향 전환 정보
L = int(input())
time = {}
for _ in range(L):
    t, d = map(str, input().split())
    time[int(t)] = d

# 큐를 이용하여 cnt(시간) 구하기
que = dq([[0,0]])
direction = 'R'
cnt = 0
while que:
    row, col = que[-1]
    # row와 col이 matrix범위를 벗어나면 break
    if row == -1 or row == N or col == -1 or col == N:
        break
    
    cnt += 1

    # 현재 방향에 따라 넣어주어야 하는 값이 다르다
    # 만약 이동한 칸이 뱀의 몸에 해당하면 자기 자신의 몸과 부딪히는 경우이므로 break
    if direction == 'R':
        if [row, col+1] in que:
            break
        que.append([row, col+1])

    elif direction == 'U':
        if [row-1, col] in que:
            break
        que.append([row-1, col])
    
    elif direction == 'D':
        if [row+1, col] in que:
            break
        que.append([row+1, col])
    
    elif direction == 'M':
        if [row, col-1] in que:
            break
        que.append([row, col-1])
    
    # 사과가 없으면 꼬리 칸을 빼준다
    if matrix[row][col] == 0:
        que.popleft()
    # 사과를 먹었으면 0으로 바꿔줘야 한다
    else:
        matrix[row][col] = 0
    
    # 방향전환을 해주는 시간이 되면 방향전환을 해준다
    if cnt in time:
        if direction + time[cnt] == 'RD' or direction+ time[cnt] == 'ML':
            direction = 'D'
        elif direction + time[cnt] == 'MD' or direction + time[cnt] == 'RL':
            direction = 'U'
        elif direction + time[cnt] == 'DD' or direction + time[cnt] == 'UL':
            direction = 'M'
        elif direction + time[cnt] == 'DL' or direction + time[cnt] == 'UD':
            direction = 'R'


# 현재 시간 출력
print(cnt)
