# 입력
N, S = map(int, input().split())
numbers = list(map(int, input().split()))

answer = 0

# 재귀함수 recur
def recur(num, idx):
    global answer
    # 부분수열의 합이 S가 되면 answer += 1
    if num == S:
        answer += 1
    
    # 현재 인덱스 다음의 숫자를 더한 경우마다 재귀함수 실행
    for i in range(idx+1, N):
        new_num = num + numbers[i]
        recur(new_num, i)

# 각 원소를 시작 숫자로 하는 경우마다 재귀함수 실행
for i, num in enumerate(numbers):
    recur(num, i)

# 출력
print(answer)