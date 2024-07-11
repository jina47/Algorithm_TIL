def findPath(path, L):
    value = path[0]
    i = 1
    end = -1
    while i < len(path):
        if path[i] == value:
            i += 1
            
        elif path[i] == value-1:
            value -= 1
            j = 0
            while j < L:
                if i+j < len(path) and path[i+j] == value:
                    j += 1
                else:
                    return False
            i += L
            end = i-1

        elif path[i] == value+1:
            j = 1
            while j <= L:
                if j <= i and i-j > end and path[i-j] == value:
                    j+=1
                else:
                    return False
            end = i-1
            i += 1
            value += 1

        else:
            return False
    return True


if __name__ == "__main__":
    N, L = map(int, input().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))

    cnt = 0

    for r in range(N):
        row = maps[r]
        cnt += findPath(row, L)

    for c in range(N):
        col = []
        for r in range(N):
            col.append(maps[r][c])
        cnt += findPath(col, L)

    print(cnt)