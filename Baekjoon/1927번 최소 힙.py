import sys
import heapq

N = int(input())
arr = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(arr, x)
    elif x == 0:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
