def solution(n, words):
    ls = [0] * n
    s = []
    for i, w in enumerate(words):
        if len(s)!= 0:
            if w[0] != s[-1][-1]:
                break

        if w not in s:
            s.append(w)
            ls[i%n] += 1
        else:
            break

    if words == s:
        return [0,0]
    else:
        for i, l in enumerate(ls):
            if l == min(ls):
                return [i+1,l+1]
