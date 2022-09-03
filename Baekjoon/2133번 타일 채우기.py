# 입력
N = int(input())

# N=2, 3 = 3
# N=4, 3*3 + 2 = 11
# N=6, 11*3 + 3*2 + 2 = 41
# N=8, 41*3 + 11*2 + 3*2 = a
# N=10, a*3 + 41*2 + 11*2 + 3*2

dp = [0, 0, 3]
for i in range(3, N+1):
    # i이 홀수인 경우는 주어진 타일로 채울 수 없음
    if i%2 == 1:
        dp.append(0)
    # i이 짝수인 경우 dp[i] = dp[i-2]*3 + dp[i-4]*2 + ... + dp[2]*2 + 2 
    else:
        temp = dp[i-2]*3 + 2
        for j in range(i-2):
            temp += dp[j]*2
        dp.append(temp)

# 출력
print(dp[N])