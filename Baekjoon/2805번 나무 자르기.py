import sys

N, M = map(int, sys.stdin.readline().strip().split())
H = list(int(h) for h in sys.stdin.readline().strip().split())

# 이분탐색 이용
def binar(l, r):
    while l <= r:
        mid = (l + r) // 2
        tree = 0
        flag = False
        for h in H:
            if h - mid > 0:
                tree += h - mid
            if tree >= M:
                flag = True
                break
        if flag == True:
            l = mid + 1
        else:
            r = mid - 1
    return r

# 출력
if N == 1:
    print(H[0]-M)
else:
    l = 0
    r = max(H)

    print(binar(l, r))
