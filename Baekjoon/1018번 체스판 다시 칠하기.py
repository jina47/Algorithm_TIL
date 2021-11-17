# 입력값 N과 M
N, M = map(int, input().split())
chess = [input() for _ in range(N)]

ans = []
for numi in range(N-7):
    for numj in range(M-7):
        cnt = 0
        i = numi
        j = numj
        while i < numi + 8:
            # print(i, j, chess[i][j])
            if (i+j) % 2 == 0 and chess[i][j] != 'B':
                cnt += 1
            elif (i+j) % 2 == 1 and chess[i][j] != 'W':
                cnt += 1

            # print(cnt)
            j += 1
            if j == numj + 8:
                j = numj
                i += 1
    
            if i == numi + 8:
                ans.append(min(cnt, 64-cnt))



print(min(ans))
