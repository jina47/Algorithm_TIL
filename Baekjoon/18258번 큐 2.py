from collections import deque as dq
import sys
 
N = int(input())

que = dq([])
for _ in range(N):
    string = sys.stdin.readline().strip()
    if string == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif string == 'size':
        print(len(que))
    elif string == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif string == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif string == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
    else:
        num = string.split()[-1]
        que.append(num)

