from collections import deque as dq

# 입력
N = int(input())
A = list(map(int, input().split()))

dp = [10000 for _ in range(N)]
visited = [0 for _ in range(N)]
dp[0] = 0
visited[0] = 1
# bfs 이용
que = dq([[0, A[0]]])
while True:
    # 오른쪽 끝까지 가지 못했는데 que가 비어버리면 오른쪽 끝으로 가는 경우가 불가능하므로 -1 출력
    if que == dq([]):
        print(-1)
        break
    idx, x = que.popleft()
    # 오른쪽 끝에 도달한 경우 최소 횟수 출력
    if idx == N-1:
        print(dp[idx])
        break
    # 점프해서 갈 수 있는 곳 탐색
    for i in range(idx+1, idx+x+1):
        if i == N:
            break
        # dp[i]에 담긴 최소 횟수보다 더 작은 횟수로 도달 가능하면 갱신 아니라면 원래 최소 횟수 유지
        dp[i] = min(dp[i], dp[idx] + 1)
        # 방문처리 후 que에 넣어주기
        if visited[i] == 0:
            que.append([i, A[i]])
            visited[i] = 1
        
