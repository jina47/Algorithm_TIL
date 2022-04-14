import sys
import heapq

N = int(input())
arr = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(arr, [x, x])
    elif x < 0:
        heapq.heappush(arr, [-x, x])
    else:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)
