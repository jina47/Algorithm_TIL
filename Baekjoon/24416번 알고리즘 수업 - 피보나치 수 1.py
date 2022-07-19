# 재귀
# def fib(n):
#     if n == 1 or n == 2:
#         print(1)
#         return 1 # 코드 1
#     else:
#         return fib(n-1) + fib(n-2)
# 코드 1 실행횟수는 피보나치 수와 같음

# dp
def fibonacci(n):
    f = [0, 1, 1] + [0 for _ in range(3, n+1)]
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2] # 코드 2
    return f[n]
# dp는 코드2 실행 횟수가 n-2

n = int(input())
print(fibonacci(n), n-2)