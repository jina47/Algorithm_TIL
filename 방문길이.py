def solution(dirs):
    x = 0
    y = 0
    lst = []
    answer = 0
    for n in range(len(dirs)):
        if dirs[n] == 'U' and y+1 < 6:
            y += 1
            if [x, y-1, 'D'] not in lst and [x,y, dirs[n]] not in lst:
                lst.append([x, y, dirs[n]])
                answer += 1
        elif dirs[n] == 'D' and y-1 > -6 :
            y -= 1
            if [x, y+1, 'U'] not in lst and [x,y, dirs[n]] not in lst:
                lst.append([x, y, dirs[n]])
                answer += 1
        elif dirs[n] == 'L' and x-1 > -6:
            x -= 1
            if [x+1, y, 'R'] not in lst and [x,y, dirs[n]] not in lst:
                lst.append([x, y, dirs[n]])
                answer += 1
        elif dirs[n] == 'R' and x+1 < 6:
            x += 1
            if [x-1, y, 'L'] not in lst and [x,y, dirs[n]] not in lst:
                lst.append([x, y, dirs[n]])
                answer += 1
    return answer