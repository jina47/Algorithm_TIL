import sys

# 입력값 N
N = int(input())

# 좌표값 담는 리스트 X
Xlst = list(map(int, sys.stdin.readline().split()))

Xsort = sorted(Xlst)
new = dict()
i = 0
for x in Xsort:
    if x not in new.keys():
        new[x] = i
        i += 1

for x in Xlst:
    print(new[x], end=' ')


