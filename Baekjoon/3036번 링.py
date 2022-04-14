import math
import sys


N = int(input())
for i, num in enumerate(list(map(int, sys.stdin.readline().split()))):
    if i == 0:
        ring = num
    else:
        g = math.gcd(ring, num)
        print(str(ring//g) + '/' + str(num//g))


