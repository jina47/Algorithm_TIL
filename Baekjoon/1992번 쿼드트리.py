def solution(x, y, N):
    global string
    start = video[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if video[i][j] != start:
                string += '('
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                string += ')'
                return
    if start == 0:
        string += '0'
    else:
        string += '1'

# 입력
N = int(input())
video = []
for _ in range(N):
    video.append([int(s) for s in input().strip()])
string = ''
solution(0, 0, N)
print(string)
