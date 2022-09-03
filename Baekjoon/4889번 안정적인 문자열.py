idx = 1
while True:
    # 입력되는 문자열 string
    string = input()
    # string이 '-'로 이루어져있으면 break
    if string[0] == '-':
        break
    
    stack = []
    # 문자열을 바꾸는 연산의 수를 세는 cnt
    cnt = 0
    for s in string:
        # stack이 비어있을 때 현재 문자가 '{'이면 stack에 넣어주지만, '}'이면 올바른 문자열이 아니므로 괄호를 바꾸어 stack에 넣어줌
        if stack == []:
            if s == '{':
                stack.append(s)
            elif s == '}':
                cnt += 1
                stack.append('{')
        # stack에 문자가 이미 있는 경우
        else:
            # stack의 마지막 괄호와 현재 괄호 s가 안정적인 문자열이라면 stack에서 pop()
            if stack[-1] == '{' and s == '}':
                stack.pop()
            # stack의 마지막 괄호와 현재 괄호 s가 안정적인 문자열이 아니라면 stack에 s 넣어줌
            else:
                stack.append(s)

    # stack이 비어있지 않다면 stack 길이의 절반만큼 문자열을 바꾸어주어야 함
    cnt += len(stack)//2


    # 출력 - 현재 인덱스. 괄호를 바꾸는 연산 cnt 형태
    print(str(idx)+'. '+str(cnt))
    idx += 1