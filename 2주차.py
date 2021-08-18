def solution(scores):
    score = [[] for _ in range(len(scores))]
    for i, s in enumerate(scores):
        for j in range(len(scores)):
            score[j].append(s[j])
    answer = ''
    for i, s in enumerate(score):
        if s.count(s[i]) == 1 and (max(s) == s[i] or min(s) == s[i]):
            s.remove(s[i])
        grade = sum(s)/len(s)
        if  100 >= grade >= 90:
            answer += 'A'
        elif grade >= 80:
            answer += 'B'
        elif grade >= 70:
            answer += 'C'
        elif grade >= 50:
            answer += 'D'
        elif 0 <= grade < 50:
            answer += 'F'
    return answer