n, k = map(int, input().split())
worth = []
for _ in range(n):
    worth.append(int(input()))
worth.sort()

dp = [0 for _ in range(k+1)]

for coin in worth:
    for num in range(1, k+1):
        # 해당 동전으로 num원을 만드는 경우 1개 추가
        if num == coin:
            dp[num] += 1
        # coin보다 큰 가치 num원을 만드는 경우 
        # coin보다 작은 가치의 동전으로 num원을 만든 경우 + coin을 이용해 (num-coin)원을 만든 경우
        elif num > coin:
            dp[num] = dp[num] + dp[num-coin]

print(dp[-1])

        