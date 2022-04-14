import sys
import heapq

# 입력
N = int(input())
arr = []
for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x > 0:
        # 힙은 작은 숫자의 우선순위가 높아지므로 큰 숫자를 우선순위로 하기 위해 -x를 이용
        heapq.heappush(arr, [-x, x])
    elif x == 0:
        if arr:
            # 우선순위가 가장 높은 리스트 [-x, x]가 반환되므로 그 중 인덱스가 1인 값을 출력
            print(heapq.heappop(arr)[1])
        else:
            print(0)


