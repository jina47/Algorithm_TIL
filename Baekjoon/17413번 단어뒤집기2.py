from collections import deque as dq

# 앞에서 꺼내려고 deque 이용
S = dq([s for s in input()])

# 원하는 답은 answer, 뒤집어진 단어를 담는 stack
answer = ''
stack = ''

while S:
    # '<'로 시작하면 '>'까지는 뒤집지 않고 그대로 answer에 더해줌
    if S[0] == '<':
        answer += stack
        stack = ''
        answer += S.popleft()
        while S[0] != '>':
            answer += S.popleft()
    
    # '>'를 answer에 더해주지 못했으므로 더해줌
    elif S[0] == '>':
        answer += S.popleft()
    
    # 공백일 경우 answer에 stack과 공백을 더해주고 stack은 빈 문자열로 초기화
    elif S[0] ==' ':
        answer += stack + S.popleft()
        stack = ''
    
    # 문자나 숫자로 이루어진 경우 뒤집어 주어야 하므로 stack의 앞에 더해줌
    else:
        stack = S.popleft() + stack
    
# 만약 stack에 글자가 있다면 answer에 더해줌    
if stack:
    answer += stack

# 출력
print(answer)