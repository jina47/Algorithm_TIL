# 분할 정복
def solution(x, y, N):
    global white, blue
    start = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if paper[i][j] != start:
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    # 구역이 모두 같은 색으로 칠해져 있는 경우                                
    if start == 0:
        white += 1
    else:
        blue += 1

# 입력
N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

white = 0
blue = 0
solution(0, 0, N)
print(white, blue)


