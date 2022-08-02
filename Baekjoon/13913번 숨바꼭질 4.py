from collections import deque as dq

N, K = map(int, input().split())

# 수빈이가 동생보다 앞서 있다면 뒤로 1씩 가는 방법밖에 없음
if K <= N:
    print(N-K)
    for t in range(N, K-1, -1):
        print(t, end=' ')

# 수빈이가 동생보다 뒤쳐져 있다면 bfs로 시간 탐색
else:
    # 수빈이의 이동경로를 리스트로 담을 리스트 bfs
    bfs = dq([[N]])
    # 방문여부 확인
    visited = [0 for _ in range(2*K)]
    visited[N] = 1
    while bfs:
        # 수빈이의 이동경로 리스트인 lst
        lst = bfs.popleft()
        # 가장 마지막에 있었던 위치 last
        last = lst[-1]

        # last가 K라면 동생의 위치에 도달한 것이므로 출력 후 break
        if last == K:
            # 시간은 lst의 길이에서 1을 빼주면 됨 (시작점의 시간은 0)
            print(len(lst)-1)
            for t in lst:
                print(t, end=' ')
            break
        
        # 1초 동안 뒤로 가거나 앞으로 가거나 2배 위치로 갈 수 있음
        for x in [last-1, last+1, 2*last]:
            # x의 위치는 0에서 2*K 사이만 가능하고 방문하지 않은 곳이어야 함
            if 0 <= x < 2*K  and visited[x] == 0:
                bfs.append(lst + [x])
                visited[x] = 1
