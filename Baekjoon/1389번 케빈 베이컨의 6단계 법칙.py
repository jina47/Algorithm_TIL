from collections import deque as dq

# 유저의 수 N, 친구관계의 수 M
N, M = map(int, input().split())

friend = {}
for _ in range(M):
    A, B = map(int, input().split())
    # friend에 친구관계 추가
    if A not in friend.keys():
        friend[A] = [B]
    else:
        # 중복으로 추가 x
        if B not in friend[A]:
            friend[A].append(B)
    
    if B not in friend.keys():
        friend[B] = [A]
    else:
        if A not in friend[B]:
            friend[B].append(A)

# bfs 이용
def bfs(x):
    que = dq([x])
    visited = [0 for _ in range(N+1)]
    visited[x] = 1
    while que:
        p = que.popleft()
        if p in friend.keys():
            for q in friend[p]:
                if visited[q] == 0:
                    que.append(q)
                    visited[q] = visited[p] + 1
    # visited의 값을 다 더해서 N을 빼주면 케빈 베이컨의 수
    return sum(visited) - N

# 케빈 베이컨의 수가 가장 작은 사람 탐색
answer, kevin = 0, float('inf')
for i in range(1, N+1):
    temp = bfs(i)
    if temp < kevin:
        kevin = temp
        answer = i

print(answer)

