import sys

# 도시의 개수
N = int(input())

# 인접한 도시 길이 (총 N-1개)
length = list(map(int, sys.stdin.readline().split()))


# 주유소 리터당 가격 (총 N개)
oil = list(map(int, sys.stdin.readline().split()))
cost = oil[0] * length[0]

mincost = oil[0]
for i in range(1, N-1):
    if oil[i] < mincost:
        mincost = oil[i]
    cost += mincost * length[i]
print(cost)
