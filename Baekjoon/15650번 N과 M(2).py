import itertools

# 자연수 N, M
N, M = map(int, input().split())

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
numbers = [n for n in range(1, N+1)]
ans = list(itertools.combinations(numbers, M))
for a in ans:
    print(' '.join(map(str, a)))
