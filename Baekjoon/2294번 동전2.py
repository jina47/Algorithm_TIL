n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
# 중복되는 동전 제거
coins = list(set(coins))

# 10001개 이상 동전을 사용할 수 없으므로 최댓값 10001 설정
dp = [10001 for _ in range(k+1)]

for i, coin in enumerate(coins):
    for worth in range(1, k+1):
        # coin 자체의 가치가 worth인 경우
        if worth == coin:
            dp[worth] = 1
        # worth가 coin보다 큰 경우 dp[worth] 갱신
        elif worth > coin:
            dp[worth] = min(dp[worth-coin]+1, dp[worth])
    
# k원을 만들 수 있는 경우가 없을 때는 -1 출력
if dp[k] != 10001:
    print(dp[k])
else:
    print(-1)