# 입력
N = int(input())
# [T, S] 담는 times
times = []
for _ in range(N):
    times.append(list(map(int, input().split())))

# 끝내야 하는 시간 S 기준 내림차순 정렬
times.sort(key=lambda x: -x[1])

# 가장 늦게 끝마치는 시간을 start로 초기화
start = times[0][1]
# 일을 시작할 수 있는 시간 구하기
for i in range(N):
    # 일을 끝내야 하는 시간이 현재 start보다 크거나 같으면 start에서 걸린 시간을 빼줌
    if times[i][1] >= start:
        start -= times[i][0]
    # 일을 끝내야 하는 시간이 현재 start보다 작으면 start를 일을 끝내야 하는 시간에서 걸리는 시간을 빼줌
    else:
        start = times[i][1]-times[i][0]

# start가 0시보다 크면 일을 끝마칠 수 있는 것이므로 start 출력
if start >= 0:
    print(start)
# start가 0시보다 작으면 일을 끝마칠 수 없는 것이므로 -1 출력
else:
    print(-1)
