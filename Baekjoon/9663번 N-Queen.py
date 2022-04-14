def dfs(queen, row, n):
    cnt = 0

    if n == row:
        return 1

    for col in range(n):
        queen[row] = col
        for i in range(row):
            # queen[i]는 이전의 row들에 대해 설정된 값
            # queen[i]와 queen[row]가 같으면 같은 행에 있는 것
            if queen[i] == queen[row]:
                break
            # 행-행 = 열-열 이 같으면 같은 대각선상에 있는 것
            if abs(queen[i]-queen[row]) == row - i:
                break
        # for문에서 break에 걸리지 않았다면 그 다음 열에 대한 탐색
        else:
            cnt += dfs(queen, row + 1, n)
    return cnt



N = int(input())
queen = [0] * N
print(dfs(queen, 0, N))
