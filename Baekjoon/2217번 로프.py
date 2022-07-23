# 입력
N = int(input())
weights = []
for _ in range(N):
    weights.append(int(input()))

# weights를 오름차순 정렬
weights.sort()
# weights의 i번째 값과 (N-i)를 곱한 값의 최댓값 구하기
ans = 0
for i in range(N):
    if ans < weights[i]*(N-i):
        ans = weights[i]*(N-i)

# 출력
print(ans)