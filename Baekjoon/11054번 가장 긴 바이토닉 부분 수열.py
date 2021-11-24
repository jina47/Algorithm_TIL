# 수열 A의 크기 N
N = int(input())

# A 리스트 만들기
# B 리스트는 A 리스트 거꾸로 정렬한 것
A = list(map(int, input().split()))
B = list(reversed(A))

# dp 리스트 만들기
# 각 리스트의 첫 번째 요소는 A 리스트 탐색, 두 번째 요소는 B 리스트 탐색
dp = [[1,1] for _ in range(N)]

for i in range(1, N):
    for j in range(i):

        if A[i] > A[j]:
            dp[i][0] = max(dp[i][0], dp[j][0]+1)

        if B[i] > B[j]:
            dp[N-1-i][1] = max(dp[N-1-i][1], dp[N-1-j][1]+1)

dp.sort(key=lambda x:sum(x))
print(sum(dp[-1])-1)
