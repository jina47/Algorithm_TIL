def factorial(N):
    if N == 0 or N == 1 :
        return 1

    else:
        return factorial(N-1) * N

N = int(input())
print(factorial(N))