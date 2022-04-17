import sys

N, M, B = map(int, sys.stdin.readline().split())
ground = []
low = 257
high = -1

# 땅의 높이를 ground에 넣어주고 최소값을 low, 최대값을 high로 저장
for i in range(N):
    for h in sys.stdin.readline().split():
        if int(h) < low:
            low = int(h)
        if int(h) > high:
            high = int(h)
        ground.append(int(h))

# ground를 높이 기준으로 내림차순 정렬
ground.sort(reverse=True)

output = []
for height in range(low, high+1):
    # 기준 height
    block = B
    time, idx = 0, 0
    # ground의 모든 원소들에 대해 height와의 차이 탐색
    while idx < N*M:
        gap = abs(height-ground[idx])
        # 땅 높이가 height보다 크면 인벤토리에 넣어줌
        if ground[idx] > height:
            time += 2*gap
            block += gap
        # 땅 높이가 height보다 작으면 인벤토리에서 꺼내옴
        elif ground[idx] < height:
            # 만약에 block이 0보다 작거나 같으면 인벤토리에서 블록을 꺼내올 수 없음
            if block <= 0:
                break
            time += gap
            block -= gap
        idx += 1
    # 모든 땅에 대해 땅 고르기를 마친 경우 output에 [time, height] append
    if idx == N*M and block >= 0:
        output.append([time, height])

# output을 time을 기준으로 오름차순, 만약 time이 같으면 height를 기준으로 내림차순 정렬
output.sort(key=lambda x: (x[0], -x[1]))

# 출력
print(' '.join(map(str, output[0])))
