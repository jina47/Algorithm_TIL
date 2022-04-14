N = int(input())
# N까지의 소수 찾기
number = []
for num in range(2, N+1):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        number.append(num)

# 소수들이 담긴 number에서 부분합이 N인 개수 찾기
end = 0
partial = 0
cnt = 0
for start in range(len(number)):
    while partial < N and end < len(number):
        partial += number[end]
        end += 1
    if partial == N:
        cnt += 1
    partial -= number[start]

print(cnt)
