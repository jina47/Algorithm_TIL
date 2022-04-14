import math

N = int(input())

numbers = [int(input()) for _ in range(N)]
numbers.sort()

ans = []
for n in range(numbers[0]):
    g = math.gcd(numbers[0]-n, numbers[1]-n)
    if g == 1:
        continue
    i = 1
    while i < N-1:
        if math.gcd(numbers[i]-n, numbers[i+1]-n) == g:
            i += 1
        else:
            break
    if i == N-1 and g not in ans:
        ans.append(g)

for a in ans:
    print(a, end=' ')
