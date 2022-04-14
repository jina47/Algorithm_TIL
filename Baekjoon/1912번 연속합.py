# 정수 n
n = int(input())
# number 리스트에 n개의 정수 넣기
number = list(map(int, input().split()))

# number[i-1]의 값에 number[i]를 더한 값이 number[i]보다 크면 number[i]에 number[i-1]를 더해줌
for i in range(1, n):
    if number[i-1] + number[i] > number[i]:
        number[i] += number[i-1]

# number의 최댓값 출력
print(max(number))