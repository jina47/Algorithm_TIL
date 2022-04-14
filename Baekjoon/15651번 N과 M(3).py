import itertools

# 자연수 N과 M
N, M = map(int, input().split())

# 1부터 N까지 자연수 중에서 M개를 고른 수열(중복 허용)
numbers = [n for n in range(1, N+1)]
ans = list(itertools.product(numbers, repeat=M))

for a in ans:
    print(' '.join(map(str,a)))
