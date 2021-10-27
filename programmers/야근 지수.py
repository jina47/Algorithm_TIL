def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0
    else:
        works.sort()
        s = sum(works) - n
        lst = []
        m = len(works)
        i = 0
        while len(lst) != len(works):
            k = s // m
            if k < works[i]:
                lst.append(k)
                s -= k
                m -= 1
            else:
                lst.append(works[i])
                s -= works[i]
                m -= 1
            i += 1
            if m == 0:
                    break
        for l in lst:
            answer += l**2
    return answer