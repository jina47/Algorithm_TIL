import sys


T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline())
    graph = {}
    for _ in range(n):
        name, cate = sys.stdin.readline().strip().split()
        if cate not in graph:
            graph[cate] = [name]
        else:
            graph[cate].append(name)
    clothes = 1
    for cate in graph:
        clothes *= len(graph[cate])+1
    print(clothes-1)