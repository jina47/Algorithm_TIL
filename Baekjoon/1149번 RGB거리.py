import sys

# 집이 개수 N
N = int(input())

# costs에 리스트로 각 집의 비용 담기
costs = []
for i in range(N):
    costs.append(list(map(int, sys.stdin.readline().split())))

# 인덱스가 다른 전 항의 최솟값을 현재 항에 더해주는 방식 이용
for i in range(1, N):
    # 빨간집
    costs[i][0] += min(costs[i-1][1], costs[i-1][2])
    # 초록집
    costs[i][1] += min(costs[i-1][0], costs[i-1][2])
    # 파란집
    costs[i][2] += min(costs[i-1][0], costs[i-1][1])

# cost[-1]의 값은 최종 집의 색깔이 R,G,B인 경우의 최소 비용
# cost[-1]의 최솟값을 구하면 총 비용 최솟값 구할 수 있음
print(min(costs[-1]))
