def solution(n, s):
    if s // n < 1:
        return [-1]
    else:
        k = s // n
        if s % n == 0:
            return [k for _ in range(n)]
        else:
            lst = []
            m = n
            while len(lst) != n:
                lst.append(k)
                s -= k
                m -= 1
                if m == 0:
                    break
                k = s // m
            return lst