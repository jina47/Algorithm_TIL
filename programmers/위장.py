def solution(clothes):
    type = {}
    for i in clothes:
        if i[1] in list(type.keys()):
            type[i[1]].append(i[0])
        else:
            type[i[1]] = [i[0]]
    type_lst = list(type.keys())
    answer = 1
    for t in type_lst:
        answer *= len(type[t]) + 1
    return answer - 1