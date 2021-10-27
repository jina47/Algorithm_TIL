def solution(skill, skill_trees):
    c = 0
    for t in skill_trees:
        lst = []
        for k in t:
            if k in skill:
                lst.append(skill.index(k))
        p = True
        for i, l in enumerate(lst):
            if l != len(lst)-1 and (lst[0] != 0 or l+1 != lst[i+1]):
                p = False
                break
        if p == True:
            c += 1
    return c
