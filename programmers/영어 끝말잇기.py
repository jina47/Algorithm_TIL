def solution(n, words):
    ls = [0] * n
    s = []
    for i, w in enumerate(words):
        if len(s)!= 0:
            if w[0] != s[-1][-1]:
                return[(i%n)+1, ls[i%n]+1]

        if w not in s:
            s.append(w)
            ls[i%n] += 1
        else:
            return[(i%n)+1, ls[i%n]+1]
    
    if words == s:
        return [0,0]