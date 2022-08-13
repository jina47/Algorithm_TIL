# 입력
k = int(input())
signs = input().split()

answer = []

# 재귀 함수 작성
# numbers에 조건을 만족하는 숫자 담기
# 현재 numbers에 채워진 마지막 숫자 now, now의 인덱스 idx
# 현재까지 사용한 숫자 방문처리하는 visited
def recur(now, idx, visited, numbers):
    # numbers 길이가 k+1이 되면 answer에 넣어주고 return
    if len(numbers) == k+1:
        answer.append(''.join(map(str, numbers)))
        return

    # 현재 numbers에 마지막으로 채워진 인덱스 idx
    if signs[idx] == '<':
        for i in range(0, 10):
            # 부등호가 '<' 이므로 now 뒤에 들어올 숫자는 now보다 커야 하고 방문하지 않았어야 함
            if now < i and visited[i] == 0:
                # 조건 만족시 numbers에 [i] 더해주고 방문 처리
                new_numbers = numbers + [i]
                visited[i] = 1
                recur(i, idx+1, visited, new_numbers)
                # for문을 계속 돌면서 탐색해야 하므로 방문 처리 해제
                visited[i] = 0
    
    # 부등호가 '>'이면 now 뒤에 들어올 숫자는 now보다 작아야 하고 방문하지 않았어야 함
    # 위와 같은 방식으로 조건 만족시 numbers에 숫자 넣어주고 재귀 함수 실행
    elif signs[idx] == '>':
        for i in range(0, 10):
            if now > i and visited[i] == 0:
                new_numbers = numbers + [i]
                visited[i] = 1
                recur(i, idx+1, visited, new_numbers)
                visited[i] = 0

# 방문처리해줄 visited 리스트                 
visited = [0 for _ in range(10)]

# numbers에 처음 넣어줄 숫자 0~9
for i in range(0, 10):
    # 해당 숫자를 numbers에 넣어주고 방문처리
    numbers = [i]
    visited[i] = 1
    # 함수 실행 후 다음 숫자에 대해서도 똑같이 실행하기 위해 방문처리 해제
    recur(i, 0, visited, numbers)
    visited[i] = 0

# 출력 (최댓값, 최솟값 순서)
print(answer[-1])
print(answer[0])
