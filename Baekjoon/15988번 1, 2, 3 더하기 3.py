# 입력
T = int(input())
ns = []
for _ in range(T):
    ns.append(int(input()))

# 1
# 1+1, 2
# 1+1+1, 2+1, 1+2, 3
dp = [0, 1, 2, 4]
for i in range(4, max(ns)+1):
    dp.append((dp[i-1]+dp[i-2]+dp[i-3])%1000000009)

for n in ns:
    print(dp[n])
