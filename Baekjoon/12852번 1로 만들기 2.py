# 입력 N
N = int(input())

dp = [[], [1], [2, 1], [3, 1]] + [[] for _ in range(4, N+1)]

for i in range(4, N+1):
    if i % 6 == 0:
        numlist = [dp[i-1], dp[i//2], dp[i//3]]
    elif i % 3 == 0:
        numlist = [dp[i-1], dp[i//3]]
    elif i % 2 == 0:
        numlist = [dp[i-1], dp[i//2]]
    else:
        numlist = [dp[i-1]]
    # dp[i]는 numlist 중 가장 최소의 길이를 가지는 리스트에 [i]를 더해준 것
    dp[i] = [i] + min(numlist, key=lambda x: len(x))
    
# 출력   
print(len(dp[N])-1)
for x in dp[N]:
    print(x, end=' ')