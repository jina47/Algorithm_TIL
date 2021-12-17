N = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(N)]
# dp의 첫번쨰 값은 arr의 첫번째 값과 같음
dp[0] = arr[0]

# dp[i]에 대해 0~i-1까지 탐색하면서 dp[i]설정
for i in range(1, N):
    # 우선 dp[i]는 arr[i]로 설정
    dp[i] = arr[i]
    for j in range(i):
        # 만약 arr[j]보다 arr[i]가 크다면 dp[i]는 dp[i]와 dp[j]+arr[i] 중 큰 값으로 설정
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+arr[i])
# dp값 중 가장 큰 값 출력
print(max(dp))

