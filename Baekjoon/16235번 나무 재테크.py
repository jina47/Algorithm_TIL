import sys

# 입력
N, M, K = map(int, sys.stdin.readline().strip().split())
# 넣어줄 양분 담는 A
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().strip().split())))
# 나무들 나이 담는 age
age = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().strip().split())
    age[x-1][y-1].append(z)
# 양분의 변화를 담는 nutrition 
nutrition = [[5 for _ in range(N)] for _ in range(N)]

# K년 동안 반복
for year in range(K):
    # 봄
    # age에서 죽은 나무들 판별 위한 death
    death = [[-1 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            # 나무가 있으면
            if age[r][c] != []:
                # 어린 나무들부터 양분을 먹으므로 temp 생성
                temp = sorted(age[r][c])
                for idx in range(len(temp)):
                    # 양분 먹기 & 나이 증가
                    if nutrition[r][c] - temp[idx] >= 0:
                        nutrition[r][c] -= temp[idx]
                        temp[idx] += 1
                    # 양분을 다 못 먹고 죽는 나무가 생기면 death[r][c]에 나무 인덱스 저장
                    else:
                        death[r][c] = idx
                        break
                # age[r][c]에는 새로운 나무 상태인 temp 담아주기 (죽은 나무들도 포함)
                age[r][c] = temp
    # 여름
    for r in range(N):
        for c in range(N):
            if death[r][c] != -1:
                # 죽은 나무가 있는 경우 양분으로 변함
                for idx in range(death[r][c], len(age[r][c])):
                    nutrition[r][c] += age[r][c][idx]//2
                # 살아있는 나무만 age[r][c]에 담아줌
                age[r][c] = age[r][c][:death[r][c]]

    # 가을
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    for r in range(N):
        for c in range(N):
            # 나무가 있는 경우
            if age[r][c] != []:
                for idx in range(len(age[r][c])):
                    # 나무의 나이가 5의 배수인 경우 인접한 8개 칸에 나이가 1인 나무 추가
                    if age[r][c][idx] % 5 == 0:
                        for i in range(8):
                            nr = r + dr[i]
                            nc = c + dc[i]
                            if 0 <= nr < N and 0 <= nc < N:
                                age[nr][nc].append(1)
    # 겨울
    for r in range(N):
        for c in range(N):
            # 양분 추가
            nutrition[r][c] += A[r][c]


# 살아있는 나무의 개수 cnt 출력
cnt = 0
for r in range(N):
    for c in range(N):
        if age[r][c] != []:
            cnt += len(age[r][c])           
print(cnt)
