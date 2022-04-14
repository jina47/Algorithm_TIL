n = int(input())
m = int(input())
friends = []
for _ in range(m):
    friends.append(list(map(int, input().split())))
friends.sort()

visit = [0 for _ in range(n+1)]
for [a, b] in friends:
    # 직접적인 친구는 1로 표시
    if a == 1:
        visit[b] = 1
    # 친구의 친구는 2로 표시
    else:
        # a만 친구인 경우, a의 친구인 b도 초대
        if visit[a] == 1 and visit[b] != 1:
            visit[b] = 2
        # b만 친구인 경우, b의 친구인 a도 초대
        elif visit[a] != 1 and visit[b] == 1:
            visit[a] = 2

# 0이 아닌 수를 가지는 요소 개수 출력
print(n + 1 - visit.count(0))

