from itertools import permutations

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
for a in permutations(num, M):
    print(' '.join(map(str, a)))