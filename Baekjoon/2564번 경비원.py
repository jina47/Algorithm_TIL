W, H = map(int, input().split())
S = int(input())
store = []
for _ in range(S):
    store.append(list(map(int, input().split())))

[x, y] = list(map(int, input().split()))
answer = 0
for [direction, distance] in store:
    if direction == 1:
        if x == 1:
            answer += abs(distance-y)
        elif x == 3:
            answer += y+distance
        elif x == 2:
            answer += H+min(y+distance, W-y+W-distance)
        elif x == 4:
            answer += y+W-distance
    elif direction == 3:
        if x == 1:
            answer += distance+y
        elif x == 3:
            answer += abs(y-distance)
        elif x == 2:
            answer += H-distance+y
        elif x == 4:
            answer += W+min(distance+y, H-distance+H-y)
    elif direction == 2:
        if x == 1:
            answer += H+min(y+distance, W-y+W-distance)
        elif x == 3:
            answer += H-y+distance 
        elif x == 2:
            answer += abs(y-distance)
        elif x == 4:
            answer += W-distance+H-y
    elif direction == 4:
        if x == 1:
            answer += W-y+distance
        elif x == 3:
            answer += W+min(distance+y, H-y+H-distance)
        elif x == 2:
            answer += W-y+H-distance
        elif x == 4:
            answer += abs(y-distance)
    
print(answer)