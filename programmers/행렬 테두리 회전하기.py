def solution(rows, columns, queries):
    matrix = [[(i-1)*columns + j for j in range(1, columns+1)] for i in range(1, rows+1)]
    new_matrix = [[(i-1)*columns + j for j in range(1, columns+1)] for i in range(1, rows+1)]
    answer = []
    for q in queries:
        x = q[0]-1
        y = q[1]-1
        lst = []
        while x == q[0]-1 and y != q[3]-1:
            y += 1
            new_matrix[x][y] = matrix[x][y-1]
            lst.append(new_matrix[x][y])
        while x != q[2]-1 and y == q[3]-1:
            x += 1
            new_matrix[x][y] = matrix[x-1][y]
            lst.append(new_matrix[x][y])
        while x == q[2]-1  and y != q[1]-1:
            y -= 1
            new_matrix[x][y] = matrix[x][y+1]
            lst.append(new_matrix[x][y])
        while x != q[0]-1 and y == q[1]-1:
            x -= 1
            new_matrix[x][y] = matrix[x+1][y]
            lst.append(new_matrix[x][y])

        matrix = [[new_matrix[i][j] for j in range(columns)]for i in range(rows)]
        answer.append(min(lst))
    return answer