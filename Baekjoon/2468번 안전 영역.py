import sys

# dfs 실행
def dfs(matrix, visited, start, num):
    stack = [start]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while stack:
        x, y = stack.pop()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # x, y의 상하좌우를 비교해서 방문하지 않았고 matrix[nx][ny]가 num이상이라면 stack에 append
            if 0 <= nx < N and 0 <= ny < N:
                if num <= matrix[nx][ny] and visited[nx][ny] == 0:
                    stack.append([nx, ny])
    return visited
    

N = int(input())
matrix = []
numset = []
# matrix에는 높이의 값을 가진 2차원 배열 
# numset은 높이의 값을 중복해서 담지 않는 리스트
for _ in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    matrix.append(lst)
    for l in lst:
        if l not in numset:
            numset.append(l)

# 높이의 값을 넣은 numset을 오름차순 정렬해줌
numset.sort()
# answer에는 안전영역의 개수를 담아줌
answer = []
# numset의 num을 비가 와도 잠기지 않는 최소의 높이로 설정
# num마다 dfs로 탐색해 cnt를 구한 후 answer에 append
for num in numset:
    # num마다 방문여부가 달라지므로 새로 설정
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            # matrix[i][j] 값이 num 이상이고 아직 방문하지 않았다면 dfs를 실행해주어 visited를 갱신
            if matrix[i][j] >= num and visited[i][j] == 0:
                visited = dfs(matrix, visited, [i, j], num)
                cnt += 1
    answer.append(cnt)

# answer의 최댓값 출력
print(max(answer))
