T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # (x1, y1)과 (x2, y2) 사이 거리의 제곱
    l = (x1-x2)**2 + (y1-y2)**2
    # 반지름의 합의 제곱
    r3 = (r1+r2)**2
    
    # 원의 중심이 같은 경우
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        # 한 원이 다른 원 내부에 있는 경우
        if r1 < r2 and l < r2**2:
            if l < (r2-r1)**2:
                print(0)
            elif l > (r2-r1)**2:
                print(2)
            elif l == (r2-r1)**2:
                print(1)
        elif r1 > r2 and l < r1**2:
            if l < (r2-r1)**2:
                print(0)
            elif l > (r2-r1)**2:
                print(2)
            elif l == (r2-r1)**2:
                print(1)
        # 한 원이 다른 원 외부에 있는 경우
        else:
            if r3 == l:
                print(1)
            elif r3 < l:
                print(0)
            elif r3 > l:
                print(2)
