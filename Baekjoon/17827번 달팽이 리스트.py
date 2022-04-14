import sys
N, M, V = map(int, sys.stdin.readline().split())
graph = list(map(int, sys.stdin.readline().split()))
for _ in range(M):
    K = int(sys.stdin.readline())
    if K < N:
        print(graph[K])
    else:
        temp = (K-N) % (N-V+1) + V-1
        print(graph[temp])

