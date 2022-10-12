M, N = map(int, input().split())

for num in range(M, N+1):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        if num != 1:
            print(num)