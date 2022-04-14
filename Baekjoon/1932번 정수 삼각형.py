import sys

# 삼각형의 크기 n
n = int(input())

# 삼각형
tri = []
for _ in range(n):
    tri.append(list(map(int, sys.stdin.readline().split())))

# tri[i]의 각 행까지 도달하는 데 더해진 최댓값을 구해본다
for i in range(1, n):
    for j in range(len(tri[i])):
        # j가 0 일떄는 대각선 오른쪽 위에만 숫자가 존재
        if j == 0:
            tri[i][j] += tri[i-1][j]
        # j가 tri[i]의 끝일 때는 대각선 왼쪽 위에만 숫자가 존재
        elif j == len(tri[i])-1:
            tri[i][j] += tri[i-1][j-1]
        # j가 0도 아니고 tri[i]의 끝도 아닌 중간 인덱스일 때는 대각선 왼쪽 위와 대각선 오른쪽 위의 숫자 중에 큰 값을 골라 더해줌
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[-1]))