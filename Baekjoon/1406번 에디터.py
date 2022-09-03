import sys
from collections import deque as dq

start = [s for s in sys.stdin.readline().strip()]

# 커서 왼쪽은 left 큐, 커서 오른쪽은 right 큐
left = dq(start)
right = dq([])

M = int(sys.stdin.readline().strip())
# 명령 수행
for _ in range(M):
    cmd = sys.stdin.readline().strip()
    if cmd == 'L':
        if left:
            right.appendleft(left.pop())
    elif cmd == 'D':
        if right:
            left.append(right.popleft())
    elif cmd == 'B':
        if left:
            left.pop()
    else:
        word = cmd.split()[1]
        left.append(word)

# 출력
print(''.join(left)+''.join(right))
