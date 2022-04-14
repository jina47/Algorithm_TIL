# 222-풀링 함수
def pooling(matrix, N):
    temp = [[0 for _ in range(N//2)] for _ in range(N//2)]
    for x in range(0, N, 2):
        for y in range(0, N, 2):
            temp[x//2][y//2] = sorted([matrix[x][y], matrix[x+1][y], matrix[x][y+1], matrix[x+1][y+1]])[2]
    return temp

# 입력
N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

# N이 1이 될 때까지 222-풀링 반복
while N > 1:
    matrix = pooling(matrix, N)
    N //= 2

# 출력
print(matrix[0][0])