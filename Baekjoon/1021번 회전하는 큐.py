from collections import deque as dq
import sys

N, M = map(int, input().split())
number = [n for n in map(int, sys.stdin.readline().split())]

cnt = 0
arr = dq([i for i in range(1, N+1)])
i = 0
while M > 0:
    if arr[0] == number[i]:
        arr.popleft()
        M -= 1
        i += 1
    else:
        if arr.index(number[i]) <= len(arr)//2:
            arr.append(arr.popleft())
            cnt += 1
        else:
            arr.appendleft(arr.pop())
            cnt += 1
print(cnt)

