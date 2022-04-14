from collections import deque as dq
import sys

N = int(input())
que = dq([])

for _ in range(N):
    order = sys.stdin.readline().rstrip()
    if order == 'size':
        print(len(que))
    elif order == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif order == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
    else:
        if order[:5] == 'pop_f':
            if que:
                print(que.popleft())
            else:
                print(-1)
        elif order[:5] == 'pop_b':
            if que:
                print(que.pop())
            else:
                print(-1)
        elif order[:6] =='push_f':
            que.appendleft(int(order.split(' ')[-1]))
        else:
            que.append(int(order.split(' ')[-1]))

