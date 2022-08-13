# 입력
N = int(input())
P = list(map(int, input().split()))

# P[i]에 i+1개 카드를 구매할 때 지불할 금액의 최솟값 담기
for i in range(N):
    for j in range(i//2+1):
        # P[i]와 P[i-j-1]+P[j] 비교해서 최솟값 담기
        P[i] = min(P[i], P[i-j-1]+P[j])

print(P[-1])