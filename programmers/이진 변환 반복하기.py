def solution(s):
    answer = [1, s.count('0')]
    n = s.count('1')
    
    while n != 1:
        s = bin(n)
        answer[1] += s[2:].count('0')
        n = s.count('1')
        answer[0] += 1
    return answer