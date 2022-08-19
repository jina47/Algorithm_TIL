#입력
N = int(input())
S = list(map(int, input().split()))

visited = [0 for _ in range(2000001)]

# 부분 수열의 합으로 만들어지는 숫자는 visited에 1로 처리
def recur(num, idx):
    visited[num] = 1
    for i in range(idx+1, N):
        new_num = num + S[i]
        recur(new_num, i)

# S의 각 원소를 시작으로 하는 부분 수열의 합 구하기
for i in range(N):
    recur(S[i], i)

# visited 탐색해서 방문하지 않은 곳 출력
for i in range(1, 2000001):
    if visited[i] == 0:
        print(i)
        break
