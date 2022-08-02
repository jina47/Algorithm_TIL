# 사람 수 N, 친구 관계 수 M
N, M = map(int, input().split())
# 친구 관계 리스트
friends = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    if b not in friends[a]:
        friends[a].append(b)
    if a not in friends[b]:
        friends[b].append(a)

ans = 0

# dfs & 백트래킹
def dfs(lst, depth):
    global ans

    # 깊이가 5가 되면 ans=1, return
    if depth == 5:
        ans = 1
        return
    
    for num in lst:
        # 아직 방문하지 않은 친구라면
        if visited[num] == False:
            # num의 방문 여부 확인
            visited[num] = True
            # num의 친구들에 대해 dfs 실행
            dfs(friends[num], depth+1)
            # for문의 다음 친구 기준으로 dfs 실행 위해 다시 원래 방문 여부로 돌려놓아야함
            visited[num] = False

for i in range(N):
    # 친구가 있다면 dfs로 깊이가 5가 되는지 확인
    if friends[i] != []:
        # visited 갱신
        visited = [False for _ in range(N)]
        # 현재 사람은 방문했으므로 True
        visited[i] = True
        # 친구들에 대해 dfs 실행
        dfs(friends[i], 1)

    # ans가 1이라면 for문 break
    if ans == 1:
        break

# 출력
print(ans)
