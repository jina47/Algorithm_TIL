import sys

# 입력
N = int(input())
time = []
for _ in range(N):
    time.append(list(map(int, sys.stdin.readline().strip().split())))

# 회의 시작 시간 순으로 정렬
time.sort()
# 첫 번째 회의 시간은 answer에 넣어줌
answer = [time[0]]

for i in range(1, len(time)):
    # temp는 이전 회의 시간
    temp = answer[-1]

    # 현재 회의 시작 시간이 이전 회의 끝 시간보다 작은 경우
    if  time[i][0] < temp[1]:
        # 현재 회의 끝 시간이 이전 회의 끝 시간보다 작거나 같은 경우
        if time[i][1] <= temp[1]:
            # answer에 이전 회의 시간을 빼주고 현재 회의 시간을 넣어줌
            answer.pop()
            answer.append(time[i])

    # 현재 회의 시작 시간이 이전 회의 끝 시간 보다 크거나 같은 경우
    else:
        # answer에 현재 회의 시간을 넣어줌
        answer.append(time[i])

# answer 개수 출력
print(len(answer))