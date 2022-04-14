import math

N, K = map(int, input().split())

# 이항계수 = N!/(K!(N-K)!)
print(math.factorial(N)//(math.factorial(K)*math.factorial(N-K)))