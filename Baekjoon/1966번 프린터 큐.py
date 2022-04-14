from collections import deque as dq

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    priority = dq([[i, int(n)] for i, n in enumerate(input().split())])
    cnt = 0
    while True:
        if priority[0] == max(priority, key=lambda x:x[1]):
            cnt += 1
            if priority[0][0] == M:
                print(cnt)
                break
            priority.popleft()

        else:
            priority.append(priority.popleft())
        

    
