import sys

# 테스트 케이스
T = int(input())
for _ in range(T):
    n = int(input())
    # 2n개의 스티커를 담는 배열
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, sys.stdin.readline().split())))
    # n이 1이라면 dp해줄 필요 없이 최댓값 뽑아내면 됨
    if n >= 2:
        # 열의 인덱스가 1인 경우에는 왼쪽 옆과 겹치지 않는 행의 값을 더해줌
        stickers[0][1] += stickers[1][0]
        stickers[1][1] += stickers[0][0]
        # 열의 인덱스를 2부터 탐색해서 j-1, j-2에 해당하는 값들 중 왼쪽 옆의 것을 제외하여 최댓값을 본래 값에 더해줌
        for j in range(2, n):
            for i in range(2):
                if i == 0:
                    stickers[i][j] += max(stickers[1][j-1], stickers[0][j-2], stickers[1][j-2])
                elif i == 1:
                    stickers[i][j] += max(stickers[0][j-1], stickers[0][j-2], stickers[1][j-2])
    # 마지막 열의 최댓값 출력
    print(max(stickers[0][-1], stickers[1][-1]))
