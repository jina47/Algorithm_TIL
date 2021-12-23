from collections import deque as dq

# bfs 이용
def bfs(N, K):
    visited = [0] * 100001
    visited[N] = 1
    que = dq([N])
    while que:
        number = que.popleft()
        if number == K:
            return visited[number]-1
        lst = [number-1, number+1, 2*number]
        for l in lst:
            if 0 <= l <= 100000 and visited[l] == 0:
                que.append(l)
                visited[l] = visited[number] + 1


# 입력
N, K = map(int, input().split())
if N == K:
    print(0)
elif N > K:
    print(N-K)
else:
    print(bfs(N, K))

