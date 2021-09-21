def solution(s):
    s = s[1:-1]
    s = s.split('}')
    s.pop()
    
    ls = [[] for i in range(len(s))]
    for j in range(len(s)):
        a = ''
        for i in range(1, len(s[j])):
            if s[j][i].isdigit() == True:
                a += s[j][i] 
                if i == len(s[j])-1:
                    ls[j].append(a)
            elif s[j][i] == ',':
                ls[j].append(a)
                a = ''
                
    ls.sort(key=lambda x : len(x))
    
    answer = []
    for i in ls:
        for j in i:
            if j != '':
                if int(j) not in answer:
                    answer.append(int(j))

    return answer