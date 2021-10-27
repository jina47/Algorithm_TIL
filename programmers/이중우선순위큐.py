def solution(operations):
    que = []
    for o in operations:
        if o[0] == "I":
            que.append(int(''.join(o.split()[1:])))
        elif len(que) == 0:
            continue
        else:
            if o == "D 1":
                que.remove(max(que))
            else:
                que.remove(min(que))
    if len(que) == 0:
        return [0,0]
    else:
        return [max(que), min(que)]