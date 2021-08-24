import math
def solution(n, k):
    answer = []
    s = [i for i in range(1, n+1)]
    if k == 1:
        return s
    while len(answer) != n:
        if len(s) == 2:
            if k == 1:
                answer += s
            elif k == 2:
                answer += reversed(s)
            break
        else:
            p = math.factorial(len(s)-1)
            m = k // p
            if k % p == 0:
                m -= 1
            answer.append(s[m])
            s.remove(s[m])
            k -= m * p
    return answer