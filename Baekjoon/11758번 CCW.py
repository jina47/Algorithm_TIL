# 입력
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# P1P2 벡터
a, b = x2-x1, y2-y1

# P1P2 벡터가 제 2,3사분면에 존재하면 P1P2 직선보다 P3가 위에 있으면 시계, 아래에 있으면 반시계, 직선에 있으면 일직선
# P1P2 벡터가 제 1,4사분면에 존재하면 P1P2 직선보다 P3가 위에 있으면 반시계, 아래에 있으면 시계, 직선에 있으면 일직선
if a != 0:
    if (y3-y1)*a < b*(x3-x1): 
        print(-1)
    elif (y3-y1)*a > b*(x3-x1): 
        print(1)
    elif (y3-y1)*a == b*(x3-x1): 
        print(0)

# P1P2 벡터가 y축과 평행한 경우 (x1 = x2)
elif a == 0:
    # P1P2벡터가 y축과 위로 수직인 경우 P3가 x2보다 왼쪽에 있으면 반시계, 오른쪽에 있으면 시계, 같은 값이면 일직선
    if b > 0:
        if x3 < x2: 
            print(1)
        elif x3 > x2: 
            print(-1)
        elif x3 == x2: 
            print(0)
    # P1P2벡터가 y축과 아래로 수직인 경우 P3가 x2보다 왼쪽에 있으면 시계, 오른쪽에 있으면 반시계, 같은 값이면 일직선
    elif b < 0:
        if x3 < x2:
            print(-1)
        elif x3 > x2:
            print(1)
        elif x3 == x2:
            print(0)
