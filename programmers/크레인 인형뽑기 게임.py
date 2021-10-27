def solution(board, moves):
    stack = []
    j = 0
    answer = 0
    for i in moves:
        j = 0
        while j != len(board):
            if board[j][i-1] != 0:
                if stack != []:
                    if stack[-1] != board[j][i-1]:
                        stack.append(board[j][i-1])
                        board[j][i-1] = 0
                        break
                    else:
                        stack.pop()
                        board[j][i-1] = 0
                        answer += 2
                        break
                else:
                    stack.append(board[j][i-1])
                    board[j][i-1] = 0
                    break
            else:
                j += 1
    return answer