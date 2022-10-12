from itertools import permutations

N = int(input())
numbers = [num for num in range(1, N+1)]
for tp in permutations(numbers, N):
    tp = list(tp)
    print(' '.join(map(str, tp)))
