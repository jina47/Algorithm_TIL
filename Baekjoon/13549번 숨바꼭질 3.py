from collections import deque as dq

# 수빈 N, 동생 K
N, K = map(int, input().split())

# 만약 수빈이가 동생보다 더 멀리 있으면 한 칸씩 뒤로 가는 것만 가능
if N >= K:
    print(N-K)

# 동생이 수빈이보다 멀리 있는 경우 bfs 이용
else:
    # 방문 체크
    visited = [-1 for _ in range(2*K)]
    visited[N] = 0

    def bfs():
        que = dq([N])
        while que:
            now = que.popleft()
            # K에 도달하면 break
            if now == K:
                break
            
            # 앞으로 한 칸 up, 뒤로 한 칸 down, 앞으로 2배 double
            up = now + 1
            down = now - 1
            double = now*2
            for next in [up, down, double]:

                # 2*K를 넘어 가는 경우는 없음
                if 0 <= next < 2*K:
                    
                    # 만약 next가 한 번도 방문하지 않은 곳이라면 que에 넣어줌
                    if visited[next] == -1:
                        que.append(next)
                        # double은 순간이동이므로 0초, 그 외는 1초 소요
                        if next != double:
                            visited[next] = visited[now] + 1
                        else:
                            visited[next] = visited[now]
                   
                    # 만약 next가 방문한 적이 있는 곳이라면 visited[next] 갱신
                    else:
                        if next != double:
                            visited[next] = min(visited[now] + 1, visited[next])
                        else:
                            visited[next] = min(visited[now], visited[next])
    
    # bfs 실행 후 visited[K] 출력
    bfs()
    print(visited[K])
