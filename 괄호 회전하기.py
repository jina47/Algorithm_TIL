def solution(s):
    answer = 0
    for l in range(len(s)):
        left = s[l:] + s[:l]
        print(left)
        i = 0
        lst = []
        while i != len(left):
            if len(lst) != 0 and str(lst[-1]) + str(left[i]) in ['()', '[]', '{}']:
                lst.pop()
            else: 
                lst.append(left[i])
            i += 1
        if len(lst) == 0:
            answer += 1
        print(lst, answer)


s = "[](){}"
solution(s)