import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    numbers = [0] + list(map(int, sys.stdin.readline().split()))
    
    # 팀에 속하는 학생 수 team
    team = 0
    # 방문 여부 및 같은 팀 여부 확인하는 visited
    visited = [0 for _ in range(n+1)]
    # 같은 팀을 이루는 학생 수를 확인 하는 cycle
    cycle = [0 for _ in range(n+1)]

    for start in range(1, n+1):
        # 아직 방문하지 않은 학생에 대해 탐색
        if visited[start] == 0:
            # 만약 학생이 자기 자신을 선택한 경우 한 명으로만 이루어진 팀
            if numbers[start] == start:
                visited[start] = start
                team += 1
            # 학생이 자기 자신을 선택하지 않은 경우 팀을 이루는지 확인
            else:
                # dfs
                cycle[start] = 1
                student = start
                while True:
                    # 방문 여부를 체크할 때 탐색을 시작하는 학생 번호로 지정
                    visited[student] = start
                    # 현재 학생이 선택한 학생은 chosen
                    chosen = numbers[student]
                    # chosen을 방문한 적이 있는데 start와 다른 숫자를 가지고 있다면 chosen은 이미 탐색된 적이 있어 팀을 이룰 수 없으므로 break
                    if visited[chosen] != 0 and visited[chosen] != start:
                        break
                    # chosen을 탐색한 적 없다면 몇 번째로 탐색하고 있는지 기록
                    if cycle[chosen] == 0:
                        cycle[chosen] = cycle[student] + 1
                        # 다음 탐색을 위해 student 갱신
                        student = chosen
                    # chosen이 탐색된 적 있다면 팀을 이룬 것이므로 team에 학생 수 더해줌
                    else:
                        team += (cycle[student] - cycle[chosen] + 1)
                        break
    
    # 팀을 이루고 있는 학생 수가 team이므로 어느 팀에도 속하지 않는 학생 수는 n-team
    print(n-team)
