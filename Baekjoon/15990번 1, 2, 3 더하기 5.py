import sys

# 입력
T = int(sys.stdin.readline())
# 입력의 숫자들을 담을 리스트 input
input = []
for _ in range(T):
    input.append(int(sys.stdin.readline()))
# 입력의 최댓값 (dp 배열을 한 번만 만들기 위해서)
n = max(input)

# dp 배열 설정
# 리스트에 담긴 리스트는 [끝에 1이 더해지는 경우의 수, 끝에 2가 더해지는 경우의 수, 끝에 3이 더해지는 경우의 수]
dp = [[], [1, 0, 0], [0, 1, 0], [1, 1, 1]]

# n번째 인덱스까지 dp 배열 구하기 (같은 수 연속 사용 불가)
# i-1번째 경우에서 1을 더해야 함
# i-2번째 경우에서 2를 더해야 함
# i-3번째 경우에서 3을 더해야 함
# 최종 방법의 수를 1000000009로 나눈 나머지를 구하는 것이므로 매 연산에 추가
for i in range(4, n+1):
    dp.append([(dp[i-1][1]+dp[i-1][2])%1000000009, 
    (dp[i-2][0]+dp[i-2][2])%1000000009, 
    (dp[i-3][0]+dp[i-3][1])%1000000009])

# 출력 (ip번째 인덱스의 합을 1000000009로 나눈 나머지)
for ip in input:
    print(sum(dp[ip])%1000000009)