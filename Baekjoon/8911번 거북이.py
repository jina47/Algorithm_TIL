T = int(input())
for _ in range(T):
    control = input().strip()
    direction = 0
    x, y = 0, 0
    row = [0]
    col = [0]
    # 상, 하, 좌, 우 순
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for c in control:
        if c == 'F':
            x += dx[direction]
            y += dy[direction]
            row.append(x)
            col.append(y)
        elif c == 'B':
            x -= dx[direction]
            y -= dy[direction]
            row.append(x)
            col.append(y)
        elif c == 'L':
            if direction == 0 or direction == 1:
                direction += 2
            elif direction == 2:
                direction = 1
            else:
                direction = 0
        elif c == 'R':
            if direction == 2 or direction == 3:
                direction -= 2
            elif direction == 0:
                direction = 3
            else:
                direction = 2

    # 직사각형 넓이 출력
    row.sort()
    col.sort()
    print((row[-1] - row[0]) * (col[-1] - col[0]))

            






