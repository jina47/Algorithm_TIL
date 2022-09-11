from collections import deque as dq

# 1000 ~ 9999 사이 소수 찾기
visited = [-1 for _ in range(10000)]
for num in range(1000, 10000):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        # num이 소수이면 visited[num] = 0 처리
        visited[num] = 0

# bfs 함수
def bfs(start, end):
    # bfs 함수 실행마다 visited 초기화해서 사용
    new_visited = visited[:]
    # start는 방문한 소수
    new_visited[start] = 1
    que = dq([start])
    # bfs 실행
    while que:
        x = que.popleft()
        # x가 원하는 값 end라면 new_visited[end]-1 반환
        if x == end:
            return new_visited[end] - 1
        # 각 자릿수 숫자를 하나씩 바꿔서 소수인지 판별
        for i in range(4):
            for j in range(10):
                if i != 3:
                    nx = int(str(x)[:i]+str(j)+str(x)[i+1:])
                elif i == 3:
                    nx = int(str(x)[:i]+str(j))
                # nx가 소수라면 que에 넣어주고 new_visited 갱신
                if new_visited[nx] == 0:
                    que.append(nx)
                    new_visited[nx] = new_visited[x] + 1
    # bfs 실행 후 반환값이 없다면 'Impossible' 반환
    return 'Impossible'


# 입력
T = int(input())
for _ in range(T):
    start, end = map(int, input().split())
    # bfs 실행 후 출력
    print(bfs(start, end))
