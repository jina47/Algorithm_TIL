def solution(name):
    lst = []
    for n in name:
        if ord(n) <= 78:
            lst.append(ord(n) - 65)
        else:
            lst.append(91 - ord(n))
    answer = sum(lst)

    if 0 not in lst:
        answer += len(name)-1
    else:
        c = len(name) - 1
        for i,l in enumerate(lst):
            if l == 0:
                new = lst[i:] + lst[:i]
                for d in new:
                    if d != 0 :
                        if c > len(name) - new.index(d) -2 + i:
                            c = len(name) - new.index(d) - 2 + i
                        break
        answer += c
    return answer