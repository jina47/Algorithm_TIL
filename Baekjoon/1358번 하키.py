w, h, x, y, p = map(int, input().split())
players = []
for _ in range(p):
    players.append(list(map(int, input().split())))

# 링크 안에 있는 선수 찾기
cnt = 0
for [px, py] in players:
    # 가운데 직사각형
    if x <= px <= x+w and y <= py <= y+h:
        cnt += 1
    # 왼쪽 반원
    elif (px-x)**2 + (py-y-h//2)**2 <= (h//2)**2 and px <= x:
        cnt += 1
    # 오른쪽 반원
    elif (px-x-w)**2 + (py-y-h//2)**2 <= (h//2)**2 and px >= x+w:
        cnt += 1

print(cnt)