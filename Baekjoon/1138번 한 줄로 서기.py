N = int(input())
info = list(map(int, input().split()))
heights = [0 for _ in range(N)]
for height, cnt in enumerate(info):
    # 앞에서부터 0의 개수를 세어서 그 값이 cnt+1이 되면 그 자리에 현재 height+1을 넣어줌
    c = 0
    for i, j in enumerate(heights):
        if j == 0:
            c += 1
            if c == cnt + 1:
                heights[i] = height + 1
                break
print(' '.join(map(str, heights)))
