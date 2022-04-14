import math

N, M = map(int, input().split())

print(math.gcd(N, M))
print(N*M//math.gcd(N, M))