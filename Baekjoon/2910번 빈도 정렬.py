N, C = map(int, input().split())
arr = list(map(int, input().split()))
cnt = []
for a in arr:
    for c in cnt:
        if c[0] == a:
            c[1] += 1
            break
    else:
        cnt.append([a, 1])

cnt.sort(key=lambda x : -x[1])

for c in cnt:
    while c[1] > 0:
        print(c[0], end=' ')
        c[1] -= 1