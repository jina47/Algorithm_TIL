from collections import deque as dq

# 전체 사람의 수 n
n = int(input())

# 촌수 계산해야 하는 사람 
p1, p2 = map(int, input().split())

# 부모 자식 관계의 개수 m
m = int(input())

family = {}
for _ in range(m):
    # 부모 x, 자식 y
    x, y = map(int, input().split())

    # 자식이 family.keys()에 있는지 판단 후 넣어주기
    if y not in family.keys():
        family[y] = [x]
    else:
        family[y].append(x)

# p1, p2의 부모 확인 리스트 
f1 = [0 for _ in range(n+1)]
f2 = [0 for _ in range(n+1)]

# bfs 이용
def bfs(x, lst):
    que = dq([x])
    lst[x] = 1
    while que:
        child = que.popleft()
        if child in family.keys():
            for parent in family[child]:
                que.append(parent)
                lst[parent] = lst[child] + 1

bfs(p1, f1)
bfs(p2, f2)

# f1과 f2 리스트에서 인덱스 별로 탐색해서 둘 다 0이 아닌 경우 (값의 합-2)을 answer에 추가
answer = []
for i in range(n+1):
    if f1[i] != 0 and f2[i] != 0:
        answer.append(f1[i] + f2[i] -2)

# answer에 값이 있는 경우 최솟값 출력
if answer:
    print(min(answer))
else:
    print(-1)