# board에 사탕 담기
N = int(input())
board = [[] for _ in range(N)]
for i in range(N):
    ipt = input()
    board[i] = [c for c in ipt]

# 같은 행에서 연속된 같은 사탕의 개수 최댓값 세기
answer = 0
for i in range(N):
    cntt = 1
    for j in range(N-1):
        if board[i][j] == board[i][j+1]:
            cntt += 1
        else:
            if cntt > answer:
                answer = cntt
            cntt = 1
    if cntt > answer:
        answer = cntt

# 같은 열에서 연속된 같은 사탕의 개수 최댓값 세기
for j in range(N):
    ccnt = 1
    for i in range(N-1):
        if board[i][j] == board[i+1][j]:
            ccnt += 1
        else:
            if ccnt > answer:
                answer = ccnt
            ccnt = 1
    if ccnt > answer:
        answer = ccnt

# 바꿔준 열을 기준으로 한 배열 2개, 바꿔준 행의 배열에서 같은 사탕 최대 갯수 찾기
def rowcandy(board, row, col):
    global answer
    cnt = 1
    for c in range(N-1):
        if board[row][c] == board[row][c+1]:
            cnt += 1
        else:
            if cnt > answer:
                answer = cnt
            cnt = 1
    
    for c in range(col, col+2):
        cnt = 1
        for r in range(N-1):
            if board[r][c] == board[r+1][c]:
                cnt += 1
            else:
                if cnt > answer:
                    answer = cnt
                cnt = 1
        if cnt > answer:
            answer = cnt
    return 

# 바꿔준 행을 기준으로 한 배열 2개, 바꿔준 열의 배열에서 같은 사탕 최대 갯수 찾기
def colcandy(board, row, col):
    global answer
    cnt = 1
    for r in range(N-1):
        if board[r][col] == board[r+1][col]:
            cnt += 1
        else:
            if cnt > answer:
                answer = cnt
            cnt = 1
            
    for r in range(row, row+2):
        cnt = 1
        for c in range(N-1):
            if board[r][c] == board[r][c+1]:
                cnt += 1
            else:
                if cnt > answer:
                    answer = cnt
                cnt = 1
        if cnt > answer:
            answer = cnt
    return

# 같은 행에서 연속된 값 두개가 다른 사탕이라면 바꿔주기
for row in range(N):
    for col in range(N-1):
        if board[row][col] != board[row][col+1]:
            board[row][col], board[row][col+1] = board[row][col+1], board[row][col]
            rowcandy(board, row, col)
            board[row][col], board[row][col+1] = board[row][col+1], board[row][col]

# 같은 열에서 연속된 값 두개가 다른 사탕이라면 바꿔주기
for col in range(N):
    for row in range(N-1):
        if board[row][col] != board[row+1][col]:
            board[row][col], board[row+1][col] = board[row+1][col], board[row][col]
            colcandy(board, row, col)
            board[row][col], board[row+1][col] = board[row+1][col], board[row][col]

# 최대 길이 출력
print(answer)
