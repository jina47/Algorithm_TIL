import sys

# input
R, C = map(int, input().split())

# puzzle
puzzle = []
for _ in range(R):
    puzzle.append([c for c in sys.stdin.readline().rstrip()])

words = []
# [가로 방향, 세로 방향] 방문 여부 처리
visited = [[[0, 0] for _ in range(C)] for _ in range(R)]

# dfs
def dfs(r, c, i):
    stack = [[r, c]]
    word = puzzle[r][c] # 첫 문자 설정
    while stack:
        [x, y] = stack.pop()
        visited[x][y][i] = 1 # 방문 처리
        if i == 0: # 가로
            nx, ny = x, y+1
        else: # 세로
            nx, ny = x+1, y
        # 방문 안 한 문자라면 word에 더해주기
        if 0 <= nx < R and 0 <= ny < C and puzzle[nx][ny] != '#' and visited[nx][ny][i] == 0:
            stack.append([nx, ny])
            word += puzzle[nx][ny]
    # word가 두 글자 이상일 때 words에 append
    if len(word) > 1:
        words.append(word)

# puzzle 탐색
for r in range(R):
    for c in range(C):
        for i in range(2):
            # '#'가 아니고 방문 안 한 경우 dfs 실행
            if puzzle[r][c] != '#' and visited[r][c][i] == 0:
                dfs(r, c, i)

# 사전 순으로 정렬 후 첫 단어 출력
print(sorted(words)[0])