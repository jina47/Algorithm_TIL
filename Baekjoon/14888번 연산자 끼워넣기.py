import itertools

# 수의 개수
N = int(input())

A = list(map(int, input().split()))
o = list(map(int, input().split()))

operations = []
for idx, n in enumerate(o):
    if idx == 0:
        operations += ['+' for _ in range(n)]
    elif idx == 1:
        operations += ['-' for _ in range(n)]
    elif idx == 2:
        operations += ['*' for _ in range(n)]
    elif idx == 3:
        operations += ['/' for _ in range(n)]

numbers = []
for opr in itertools.permutations(operations):
    ans = 0
    for i in range(len(opr)):
        if i == 0:
            ans = A[i]

        if opr[i] == '+':
            ans += A[i+1]
        elif opr[i] == '-':
            ans -= A[i+1]
        elif opr[i] == '*':
            ans *= A[i+1]
        elif opr[i] == '/':
            if ans >= 0:
                ans //= A[i+1]
            else:
                ans = -(-ans // A[i+1])
    numbers.append(ans)

print(max(numbers))
print(min(numbers))
        