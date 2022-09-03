from heapq import heappush, heappop

# 입력
N = int(input())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))
table.sort()

        
# 강의실들 중 끝나는 시간이 작은 쪽에 새로운 시간 넣어야 함
# 모든 강의실의 끝나는 시간보다 새로 시작하는 수업의 시작 시간이 작다면 새로운 강의실 열어야 함 

# 각 강의실의 끝나는 시간을 담는 heap
heap = []

# table을 돌면서 수업을 추가한 강의실의 끝나는 시간 갱신
for i in range(N):
    # 첫 수업 첫 강의실 생성
    if i == 0:
        heappush(heap, table[0][1])
    else:
        # 강의실들 중 끝나는 시간이 가장 빠른 시간 end
        end = heappop(heap)
        # end보다 추가해야하는 수업의 시작시간이 크거나 같으면 해당 강의실의 끝나는 시간을 table[i][1]로 갱신
        if end <= table[i][0]:
            heappush(heap, table[i][1])
        # end보다 추가해야하는 수업의 시작시간이 빠르다면 새로운 강의실 생성
        else:
            heappush(heap, end)
            heappush(heap, table[i][1])

# heap의 길이는 강의실의 최소 개수
print(len(heap))

        
