# 입력
N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

answer = []
for i in range(N):
    # i+1이 answer에 있으면 판단할 필요가 없음
    if i+1 not in answer:
        # dfs로 first와 second가 같은지 판단
        first, second = [], []
        stack = [i+1]
        while stack:
            x = stack.pop()
            # x가 first에 없다면 실행
            if x not in first:
                # x 밑의 숫자가 answer에 없는데 i+1보다 작으면 사이클이 만들어지지 않으므로 break
                if numbers[x-1] not in answer and numbers[x-1] < i+1:
                    break
                first.append(x)
                second.append(numbers[x-1])
                stack.append(numbers[x-1])
        first.sort()
        second.sort()
        # first와 second가 같으면 answer에 first를 더해줌
        if first == second:
            answer += first

# 출력
print(len(answer))
answer.sort()
for a in answer:
    print(a)

