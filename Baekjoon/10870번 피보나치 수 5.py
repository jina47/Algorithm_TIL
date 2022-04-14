def Fibo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return Fibo(N-2) + Fibo(N-1)

N = int(input())
print(Fibo(N))