def solution(lottos, win_nums):
    num = 0
    known = [i for i in lottos if i != 0]
    for i in known:
        if i in win_nums:
            num += 1

    m_n = [num + 6-len(known), num]
    answer = []
    for j in m_n:
        if j >= 2:
            answer.append(7-j)
        else:
            answer.append(6) 
    return answer