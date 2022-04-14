import sys

N, M = map(int, input().split())
train = [[0 for _ in range(20)] for _ in range(N)]
# 명령 수행
for _ in range(M):
    temp = list(map(int, sys.stdin.readline().split()))
    if temp[0] == 1:
        train[temp[1]-1][temp[2]-1] = 1
    elif temp[0] == 2:
        train[temp[1]-1][temp[2]-1] = 0
    elif temp[0] == 3:
        train[temp[1]-1] = [0] + train[temp[1]-1][:-1]
    elif temp[0] == 4:
        train[temp[1]-1] = train[temp[1]-1][1:] + [0]

# 은하수를 건너는 기차 목록
answer = []
for i in range(N):
    if train[i] not in answer:
        answer.append(train[i])

# 은하수를 건너는 기차의 수 출력
print(len(answer))