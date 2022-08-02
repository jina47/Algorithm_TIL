from collections import deque as dq
import sys

N = int(sys.stdin.readline())
que = dq([])
for _ in range(N):
    cmds = sys.stdin.readline()
    if cmds[:2] == 'pu':
        num = int(cmds.split()[-1])
        que.append(num)
    elif cmds[:2] == 'po':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif cmds[:2] == 'si':
        print(len(que))
    elif cmds[:2] == 'em':
        if que:
            print(0)
        else:
            print(1)
    elif cmds[:2] == 'fr':
        if que:
            print(que[0])
        else:
            print(-1)
    elif cmds[:2] == 'ba':
        if que:
            print(que[-1])
        else:
            print(-1)

