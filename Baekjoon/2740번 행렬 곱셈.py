N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))

for k in range(N):
    lst = []
    for j in range(K):
        num = 0
        for i in range(M):
            num += A[k][i] * B[i][j]
        lst.append(str(num))
    print(' '.join(lst))

