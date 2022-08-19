# 입력
n = int(input())
array = list(map(int, input().split()))

# new_array에 해당 인덱스까지의 수열 중 [제거 없는 연속 합, 제거 있는 연속 합] 담아주기
new_array = [[array[0], 0]]
for i in range(1, n):
    new_array.append([max(new_array[i-1][0]+array[i], array[i]), max(new_array[i-1][0], new_array[i-1][1]+array[i])])

# new_array 중 최댓값 구하기 (0항1열 제외)
answer = new_array[0][0]
for i in range(1, n):
    if answer < max(new_array[i]):
        answer = max(new_array[i])
print(answer)