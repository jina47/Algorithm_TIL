T = int(input())
for _ in range(T):
    l, n = map(int, input().split())
    bridge = [[] for _ in range(l+1)]
    for _ in range(n):
        ant = int(input())