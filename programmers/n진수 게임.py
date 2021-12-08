# n진수로 바꾼 숫자를 문자열에 더해줘서 return
def trans(n, number):
    graph = ['0','1','2','3','4','5','6','7','8','9','A','B', 'C', 'D', 'E', 'F']
    numlst = ''
    for i in range(number+1):
        temp = ''
        while True:
            b = i % n
            temp = graph[b] + temp
            if i // n == 0:
                break
            else:
                i //= n
        numlst += temp
    return numlst

# 원하는 답 출력
def solution(n, t, m, p):
    string = trans(n, m*t)
    answer = ''
    # t개만 출력하면 되므로 string에서 골라 answer에 더해주고 return
    for idx in range(t):
        answer += string[p-1+idx*m]
    return answer
