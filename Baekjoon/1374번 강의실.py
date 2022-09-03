from heapq import heappush, heappop

N = int(input())
room = []
for _ in range(N):
    room.append(list(map(int, input().split())))
# 수업 시작 시간 기준 오름차순 정렬
room.sort(key=lambda x: x[1])

# 수업 종료 시간과 새로운 수업 시작 시간 비교해서 강의실 지정
heap = [room[0][2]]
for i in range(1, N):
    end = heappop(heap)
    # 현재 주어진 강의실의 수업 종료시간 보다 새로운 수업 시작 시간이 더 느린 경우 강의실에서 수업 진행 가능
    if room[i][1] >= end:
        heappush(heap, room[i][2])
    # 현재 주어진 강의실의 수업 종료시간 보다 새로운 수업 시작 시간이 더 빠른 경우 새로운 강의실 개설    
    else:
        heappush(heap, room[i][2])
        heappush(heap, end)

# 출력
print(len(heap))

