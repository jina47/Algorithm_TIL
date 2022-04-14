import math

N = int(input())

# N까지의 숫자 중 5가 몇 번 곱해지는지 카운트
cnt = 0
for num in range(1, N+1):
    if num % 125 == 0:
        cnt += 3
    elif num % 25 == 0:
        cnt += 2
    elif num % 5 == 0:
        cnt += 1
print(cnt)
