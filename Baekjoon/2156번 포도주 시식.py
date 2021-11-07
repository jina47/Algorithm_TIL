import sys

# 포도주 잔 개수 n
n = int(input())

# 포도주 양 리스트로 만들기
wine = []
for _ in range(n):
    wine.append(int(sys.stdin.readline()))

# 마실 수 있는 포도주의 양 최댓값 구하기
# amount의 요소들은 [[i-2] 포도주 잔을 선택하고 [i] 포도주 잔 선택하는 경우, [i-1] 포도주 잔 선택하고 [i] 포도주 잔 선택하는 경우]
amount = [[0,0], [wine[0], 0]]
# 첫 번째 요소 : amount[i-2]까지의 값들 중 최댓값(temp)을 wine[i-1]과 더해준 값
# 두 번째 요소 : amount[i-1]의 값 중 첫 번째 값에 wine[i-1] 더해준 값
temp = 0
for i in range(2, n+1):
    if temp < max(amount[i-2]):
        temp = max(amount[i-2])
    amount.append([temp + wine[i-1], amount[i-1][0] + wine[i-1]])

# amount 값들 중 최댓값 출력
answer = 0
for w in amount[-3:]:
    if answer < max(w):
        answer = max(w)
print(answer)
