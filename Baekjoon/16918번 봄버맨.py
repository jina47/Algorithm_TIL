import sys

### 첫 번째 풀이 ###

R, C, N = map(int, input().split())
matrix = [[] for _ in range(R)]
# 폭탄이 있으면 1, 없으면 0으로 표현
# 리스트의 두번째 값은 시간을 표현
for i in range(R):
    ipt = input().strip()
    for b in ipt:
        if b == '.':
            matrix[i].append([0, 0])
        elif b == 'O':
            matrix[i].append([1, 0])

# 시간이 1초일 때는 처음 모습과 같고
# 그 후의 시간에 대해서는 2, 3, 4, 5초에 해당하는 matrix가 반복된다
# 따라서 answer에 5초까지의 결과를 담는다
second = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = [[],[],[],[],[]]
while second < 5:
    # 매초마다 방문여부를 체크해주어야 한다
    visited = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            # 만약 폭탄이 있다면 시간이 1초이거나 2초일 때는 시간을 하나 더해준다
            if matrix[r][c][0] == 1:
                if matrix[r][c][1] == 0 or matrix[r][c][1] == 1:
                    matrix[r][c][1] += 1
                # 시간이 3초 일 때는 상하좌우에 폭탄이 있다면 함께 터진다
                elif matrix[r][c][1] == 2:
                    for i in range(4):
                        nx = r + dx[i]
                        ny = c + dy[i]
                        # 상하좌우에 matrix값이 [1,2]가 아닌 폭탄이 함께 터진다
                        if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny][0] == 1 and matrix[r][c][1] != matrix[nx][ny][1]:
                            visited[nx][ny] = 1
                            matrix[nx][ny] = [0, 1]
                    # 터지고 난 폭탄은 [0, 1]로 리셋해주고 방문했다고 표시해준다
                    matrix[r][c] = [0, 1]
                    visited[r][c] = 1
            # 만약 방문하지 않았고 폭탄도 없다면 초기에 [0, 0]이었다면 [0, 1]로 만들어줌
            elif matrix[r][c][0] == 0 and visited[r][c] == 0:
                if matrix[r][c][1] == 0:
                    matrix[r][c][1] += 1
                # 폭탄이 없었던 곳([0,1])에는 폭탄을 넣어주고([1,0]) 방문했다고 표시해주어야 새로 바뀐 값에 대해 폭탄이 터지지 않는다
                else:
                    matrix[r][c] = [1, 0]  
                    visited[r][c] = 1                  
    
    # second에 해당하는 인덱스에 현재 matrix값을 넣어준다
    answer[second] = [m[:] for m in matrix]
    second += 1

# 만약 N이 1이라면 answer[0]
if N == 1:
    num  = 0
# N이 그 이상의 값이라면 4로 나눈 나머지가 2, 3 이면 answer[1], answer[2]를, 나머지가 0, 1이라면 answer[3], answer[4]를 이용해 현재 상태 표시
else:
    num = N % 4
    if num >= 2:
        num -= 1
    else:
        num += 3
# 출력
for j in range(R):
    for k in range(C):
        if answer[num][j][k][0] == 0:
            print('.', end = '')
        else:
            print('O', end = '')
    print()



### 두 번째 풀이 ###

R, C, N = map(int, input().split())
# 0, 1초의 상태
board = []
for _ in range(R):
    board.append(list(s for s in sys.stdin.readline().strip()))

# 5, 9, 13 .. 초의 상태
board1 = [['O' for _ in range(C)] for _ in range(R)]
# 짝수 초의 상태
board2 = [['O' for _ in range(C)] for _ in range(R)]
# 3, 7, 11 .. 초의 상태
board3 = [['O' for _ in range(C)] for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 첫 번째 폭탄이 터졌을 때
for r in range(R):
    for c in range(C):
        # 폭탄이 있으면 다음 번에 터진 상태
        if board[r][c] == 'O':
            board3[r][c] = '.'
        else:
            # 폭탄이 터진 상태인데 상하좌우 폭탄이 하나라도 있으면 다음 번에도 터진 상태 유지
            for i in range(4):
                nr = r + dx[i]
                nc = c + dy[i]
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != '.':
                    board3[r][c] = '.'
                    break
# 두 번째 폭탄이 터졌을 때
for r in range(R):
    for c in range(C):
        # 폭탄이 있으면 다음 번에 터진 상태
        if board3[r][c] == 'O':
            board1[r][c] = '.'
        else:
            # 폭탄이 터진 상태인데 상하좌우 폭탄이 하나라도 있으면 다음 번에도 터진 상태 유지
            for i in range(4):
                nr = r + dx[i]
                nc = c + dy[i]
                if 0 <= nr < R and 0 <= nc < C and board3[nr][nc] != '.':
                    board1[r][c] = '.'
                    break

# N = 1초인 경우
if N <= 1:
    for r in range(R):
        print(''.join(board[r]))
else:
    # N = 5, 9, 13 .. 초의 경우
    if N % 4 == 1:
        for r in range(R):
            print(''.join(board1[r]))
    # N = 3, 7, 11 .. 초의 경우
    elif N % 4 == 3:
        for r in range(R):
            print(''.join(board3[r]))
    # N = 짝수인 경우
    else:
        for r in range(R):
            print(''.join(board2[r]))