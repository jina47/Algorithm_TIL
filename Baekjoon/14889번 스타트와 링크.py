import itertools

N = int(input())

# 능력치 2차원 배열로 저장
performs = []
for _ in range(N):
    performs.append(list(map(int, input().split())))

# comb에 1부터 N까지의 수를 두 그룹으로 나누기 위해 combinations이용
comb = list(itertools.combinations([i for i in range(1, N+1)], N//2))

diff = []
for i in range(len(comb)//2):
    # start는 comb[i]에 있는 번호끼리 팀인 경우 능력치의 합
    start = 0
    for u in comb[i]:
        for v in comb[i]:
            if u != v:
                start += performs[u-1][v-1]
    # link는 comb[len(comb)-i-1]에 있는 번호끼리 팀인 경우 능력치의 합
    link = 0
    for x in comb[len(comb)-i-1]:
        for y in comb[len(comb)-i-1]:
            link += performs[x-1][y-1]
    # start와 link의 차이를 diff에 저장
    diff.append(abs(start-link))
# diff의 최솟값 출력
print(min(diff))
