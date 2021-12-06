# dfs 실행
def dfs(matrix, graph, idx):
    visited = [0 for _ in range(N+1)]
    [start, end] = idx
    stack= [start]
    cnt = 0
    while stack:
        node = stack.pop()
        # start는 다른 지점으로 갔다가 돌아오는 경우에 방문한 것
        if cnt != 0:
            visited[node] = 1
        # node가 end이면 matrix[start][end] = 1
        # cnt가 0이면 start에서 다른 지점으로 이동하지 않은 것이므로 matrix값은 0이어야 함
        if node == end and cnt != 0:
            matrix[start][end] = 1
            return
        # graph에 node가 있으면 인접노드 stack에 append
        if node in graph:
            for nextnode in graph[node]:
                if visited[nextnode] == 0:
                    stack.append(nextnode)
                    cnt += 1
    return

# 입력
N = int(input())
graph = {}
matrix = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            matrix[i][j] = temp[j]
            if i not in graph:
                graph[i] = [j]
            else:
                graph[i].append(j)

# 인접행렬 구하기
for n in range(N):
    for m in range(N):
        idx = [n, m]
        dfs(matrix, graph, idx)

# 출력
for t in matrix:
    print(' '.join(map(str, t)))
