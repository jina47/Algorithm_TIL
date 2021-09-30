import sys

n = int(input()) # 입력 데이터 수

for _ in range(n):
    data = sys.stdin.readline().strip()
    
    # data 길이가 홀수라면 올바른 괄호 문자열이 될 수 없으므로 무조건 'NO' print
    if len(data) % 2 != 0:
        print('NO')
        continue
    
    # data길이가 짝수라면 stack을 만들어서 판단
    stack = []
    
    for temp in data:
      
        # stack의 맨 끝 값이 '('이고 stack에 들어갈 값이 ')'인 경우 올바른 괄호 문자열이므로 stack의 끝 값을 제거
        if len(stack) != 0 and stack[-1] == '(' and temp == ')':
            stack.pop()
            
        # 그렇지 않은 경우 stack에 data 첫 문자 추가    
        else: 
            stack.append(temp) 
        
    # 모든 과정 후 stack에 아무런 값도 없다면 올바른 괄호 문자열     
    if len(stack) == 0: 
        print('YES')
        
    # stack에 값이 남아 있다면 올바르지 않은 괄호 문자열
    else: 
         print('NO')
