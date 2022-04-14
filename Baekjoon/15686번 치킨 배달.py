import sys
from itertools import combinations

def path(city, chicken, comb, house):
    global answer
    
    distance = 0
    for [j, k] in house:
        # house의 인덱스 값 하나와 comb로 뽑힌 치킨의 인덱스 값들의 차이 중 가장 작은 것을 뽑아 distance에 더해줌
        temp = []
        for idx in comb:
            [row, col] = chicken[idx]
            temp.append(abs(j-row)+abs(k-col))
        distance += min(temp)
        # 만약 answer은 0이 아니고 distance가 answer보다 크면 더 구할 필요가 없으므로 answer return
        if answer != 0 and distance > answer:
            return answer
    # answer보다 작은 distance return
    return distance



# 입력
N, M = map(int, sys.stdin.readline().split())
city = []
for _ in range(N):
    city.append(list(map(int, sys.stdin.readline().split())))

chicken = []
house = []
for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            house.append([r, c])
        elif city[r][c] == 2:
            chicken.append([r, c])

answer = 0
# 치킨집의 인덱스 중 M개를 뽑아 path함수로 distance 구하기
for comb in combinations(range(len(chicken)), M):
    answer = path(city, chicken, comb, house)
# answer에 가장 작은 최단 거리 저장되어있으므로 answer 출력
print(answer)