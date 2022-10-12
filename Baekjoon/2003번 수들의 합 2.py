N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
    total = 0
    for j in range(i, N):
        if total < M:
            total += A[j]
        elif total >= M:
            break
    if total == M:
        cnt += 1
print(cnt)