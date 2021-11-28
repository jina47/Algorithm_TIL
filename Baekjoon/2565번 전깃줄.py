# 전깃줄 개수
N = int(input())

# A, B 전봇대의 값을 electrics에 담기
electrics = []
for _ in range(N):
    electrics.append(list(map(int, input().split())))

# A 전봇대 기준으로 오름차순 정렬
electrics.sort()

# dp로 B 전봇대를 나열한 리스트 중 가장 긴 수열의 길이 구하기
dp = [1 for _ in range(N)]
for i in range(1, N):
    for j in range(i):
        if electrics[i][1] > electrics[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))
