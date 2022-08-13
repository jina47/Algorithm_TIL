# 입력
N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))


# 두 팀 사이 능력치 gap은 아무리 커도 400을 넘지 않는다
gap = 400

# gap 구하는 함수, 재귀 이용
def cal_gap(visited, idx):
    global gap

    # start, link값 구하기
    start, link = 0, 0
    # visited[i]가 0이라면 link팀, visited[i]가 1이라면 start팀
    for i in range(N):
        if visited[i] == 0:
            for j in range(N):
                if visited[j] == 0:
                    link += S[i][j]
        if visited[i] == 1:
            for j in range(N):
                if visited[j] == 1:
                    start += S[i][j]
    
    # gap 갱신
    if abs(link-start) < gap:
        gap = abs(link-start)
    
    # 현재 인덱스 다음부터 visited[i]가 0이면 방문처리 후 재귀 함수 실행
    for i in range(idx+1, N):
        if visited[i] == 0:
            visited[i] = 1
            cal_gap(visited, i)
            # 다음 경우를 위해 다시 방문하지 않은 것으로 처리
            visited[i] = 0


# 방문 여부 나타내는 visited
visited = [0 for _ in range(N)]
# 1번(인덱스 0) 사람이 속해 있는 팀을 스타트팀으로 설정(방문 처리된 팀)
visited[0] = 1

# gap 구하는 함수 실행
cal_gap(visited, 0)

# 출력
print(gap)