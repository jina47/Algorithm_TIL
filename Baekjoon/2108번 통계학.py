import sys

# 입력값 N 홀수
N = int(input())

# 숫자들 담는 numbers 리스트
numbers = [int(sys.stdin.readline()) for _ in range(N)]
# 오름차순으로 정렬
numbers.sort()

# 산술평균 출력
print(round(sum(numbers)/N))

# 중앙값 출력
print(numbers[N//2])

# 최빈값 출력
cnt = dict()
for num in numbers:
    if num not in cnt.keys():
        cnt[num] = 1
    else:
        cnt[num] += 1

frequent = []
fmax = max(cnt.values())
for key, value in cnt.items():
    if value == fmax:
        frequent.append(key)
    if len(frequent) == 2:
        break
if len(frequent) < 2:
    print(frequent[0])
else:
    print(frequent[1])
        

# 범위 출력
print(numbers[-1]-numbers[0])
