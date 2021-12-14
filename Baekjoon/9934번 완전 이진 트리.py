from collections import deque as dq

K = int(input())
buildings = list(map(int, input().split()))

# 인덱스와 레벨을 이용해서 bfs 실행
answer = [[] for _ in range(K)]
que = dq([[(2**K-1)//2, 0]])
while que:
    [idx, level] = que.popleft()
    if level == K:
        break
    answer[level].append(buildings[idx])
    que.append([idx-2**(K-2-level), level+1])
    que.append([idx+2**(K-2-level), level+1])

# 출력
for a in answer:
    print(' '.join(map(str, a)))
