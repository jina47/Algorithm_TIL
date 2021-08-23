def solution(genres, plays):
    genre_dict = {}
    for i, p in enumerate(plays):
        if genres[i] in genre_dict.keys():
            genre_dict[genres[i]].append([p, i])
            genre_dict[genres[i]][0] += p
        else:
            genre_dict[genres[i]] = [p, [p, i]]

    answer = []
    for g in sorted(genre_dict.values(), reverse=True):
        rank = sorted(g[1:], reverse=True)
        k = rank[0][0]
        lst = []
        for r in rank:
            if r[0] == k:
                lst.append(r[1])
                lst = sorted(lst)[:2]
            elif len(lst) < 2:
                lst.append(r[1])
        for l in lst:
            answer.append(l)

    return answer