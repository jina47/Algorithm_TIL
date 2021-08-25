def solution(triangle):
    x = 1
    y = 0
    while x != len(triangle):
        for y in range(len(triangle[x])):
            if x == 1:
                triangle[x][y] += triangle[0][0]
            elif y == 0 :
                triangle[x][y] += triangle[x-1][y]
            elif y == len(triangle[x])-1:
                triangle[x][y] += triangle[x-1][y-1]
            else:
                triangle[x][y] += max(triangle[x-1][y], triangle[x-1][y-1])
        x += 1
    return max(triangle[-1])