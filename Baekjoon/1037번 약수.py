
# 약수의 개수 N
N = int(input())

numbers = sorted(list(map(int, input().split())), reverse=True)

if N % 2 == 1:
    print(numbers[N//2]**2)
else:
    print(numbers[0] * numbers[-1])
