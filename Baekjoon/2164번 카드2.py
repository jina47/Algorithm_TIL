from collections import deque as dq

N = [i for i in range(1, int(input())+1)]
queue = dq(N)
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])

