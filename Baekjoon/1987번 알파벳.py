# 시간초과 나버림....
# def dfs(board, alphabet, start):
#     global R, C
#     [r, c] = start
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     stack = [[r, c]]
#     while stack:
#         [x, y] = stack.pop()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < R and 0 <= ny < C:
#                 for alpha in alphabet:
#                     if alpha == board[nx][ny]:
#                         answer.append(len(alphabet))
#                         break
#                 else:
#                     stack.append([nx, ny])
#                     dfs(board, alphabet + [board[nx][ny]], [nx, ny])
# 
# 이건 자꾸 중복 수행. . .  
# def dfs(board, start):
#     length = [[0 for _ in range(C)] for _ in range(R)]
#     [r, c] = start
#     alphabet = [board[r][c]]
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     stack = [[r, c]]
#     while stack:
#         [x, y] = stack.pop()
#         length[x][y] += 1
#         alphabet = alphabet[:length[r][c]]
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < R and 0 <= ny < C:
#                 for alpha in alphabet:
#                     if board[nx][ny] == alpha:
#                         answer.append(length[nx][ny])
#                         break
#                 else:
#                     alphabet.append(board[nx][ny])
#                     length[nx][ny] = length[x][y]
#                     stack.append([nx, ny])
        



R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append([s for s in input().strip()])

if R == 1 and C == 1:
    print(1)
else:
    answer = []
    alphabet = [board[0][0]]
    dfs(board, [0, 0])
    print((answer))

