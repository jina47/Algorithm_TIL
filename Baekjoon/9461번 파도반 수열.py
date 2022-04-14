# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 N 리스트
N = [int(input()) for _ in range(T)]

# P(N) 구하기
P = [1, 1, 1, 2, 2]
m = max(N)
if m >= 5:
    for i in range(5, m):
        P.append(P[i-1] + P[i-5])

for num in N:
    print(P[num-1])