T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        # 출발점이 해당 행성계에 있는 경우 cnt += 1
        if (x1-cx)**2 + (y1-cy)**2 < r**2:
            cnt += 1
            # 출발점과 도착점 모두 해당 행성계에 있는 경우 cnt -= 1
            if (x2-cx)**2 + (y2-cy)**2 < r**2:
                cnt -= 1
        # 출발점은 없고 도착점은 해당 행성계에 있는 경우 cnt += 1
        else:
            if (x2-cx)**2 + (y2-cy)**2 < r**2:
                cnt += 1
    print(cnt)
