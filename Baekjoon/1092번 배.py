from heapq import heappush, heappop

# 입력
N = int(input())
crane = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

# crane과 box 내림차순 정렬
crane.sort(reverse=True)
box.sort(reverse=True)

# 배로 옮길 수 없는 경우
if box[0] > crane[0]:
    print(-1)

# 모든 박스를 옮기는데 드는 최소 시간 출력
else:
    # crane[idx] 이하 crane[idx+1] 초과 무게를 가진 박스의 개수를 cnt[idx]에 담음
    cnt = [0]
    idx = 0
    for i in range(M):
        if idx == N-1:
            cnt[idx] += 1
        # 무게가 crane[idx+1]보다 크고 crane[idx] 이하의 박스는 cnt[idx]에 카운트 
        elif crane[idx+1] < box[i] <= crane[idx]:
            cnt[idx] += 1
        else:
            idx += 1
            if idx == N:
                break
            cnt.append(1)
    
    # cnt 분배
    answer = [cnt[0]]
    for i in range(1, len(cnt)):
        # cnt[i]가 max(answer) 이상인 경우
        if max(answer) <= cnt[i]:
            # cnt[i]//(i+1)과 answer의 최댓값 비교해서 큰 값 temp을 answer에 넣어줌
            temp = max(cnt[i]//(i+1), max(answer))
            heappush(answer, temp)
            # temp에서 answer에 담아준 박스의 개수 빼줌
            temp = cnt[i] - temp
            # 더 분배해야 하는 박스가 있다면 temp가 0이 될 때까지 answer의 최솟값에 1씩 더해줌
            while temp > 0:
                heappush(answer, heappop(answer)+1)
                temp -= 1
        # cnt[i]가 max(answer)보다 작은 경우 cnt[i] 넣어줌
        else:
            heappush(answer, cnt[i])
    
    # answer의 최댓값 출력
    print(max(answer))
            

