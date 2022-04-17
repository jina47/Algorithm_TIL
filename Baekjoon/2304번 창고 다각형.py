# 입력
N = int(input())

# 기둥들 위치 순으로 정렬
bars = []
for _ in range(N):
    bars.append(list(map(int, input().split())))
bars.sort()

area = 0

# 앞에서부터 커지는 기둥 고려
for i in range(N):
    if i == 0:
        top = [0, bars[0][1]]
        continue
    # 더 큰 기둥이 나오면 area += top의 기둥높이 * (현재 기둥위치와 top에 저장된 기둥위치) 
    # 그 후 top에 현재 [인덱스, 기둥높이] 저장
    if bars[i][1] >= top[1]:
        area += top[1] * (bars[i][0] - bars[top[0]][0])
        top = [i, bars[i][1]]

# 가장 큰 기둥이 있는 곳 면적 더해주기
area += top[1]

# 뒤에서부터 커지는 기둥 고려 (top에 저장된 인덱스까지만 탐색)
for i in range(N-1, top[0]-1, -1):
    if i == N-1:
        bottom = [N-1, bars[N-1][1]]
        continue
    # 더 큰 기둥이 나오면 area += bottom의 기둥높이 * (현재 기둥위치와 bottom에 저장된 기둥위치) 
    # bottom에 현재 [인덱스, 기둥높이] 저장
    if bars[i][1] >= bottom[1]:
        area += bottom[1] * (bars[bottom[0]][0] - bars[i][0])
        bottom = [i, bars[i][1]]

# 출력
print(area)