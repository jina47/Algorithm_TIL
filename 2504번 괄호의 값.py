string = [s for s in input()]

# string의 길이가 홀수면 올바른 괄호열이 아님
if len(string) % 2 != 0 :
    print(0)

# string의 첫 문자가 ')'이거나 ']' 라면 올바른 괄호열이 아님
elif string[0] == ')' or string[0] == ']':
    print(0)

# string의 끝 문자가 '('이거나 '[' 라면 올바른 괄호열이 아님
elif string[-1] == '(' or string[-1] == '[':
    print(0)

# '[]'와 '()'의 짝 개수가 맞지 않으면 올바른 괄호열이 아님
elif string.count('[') != string.count(']') or string.count('(') != string.count(')'):
    print(0)

else:
    # stack을 이용해서 괄호열 계산
    # stack에 string[0]을 넣어줌
    stack = [string[0]]

    # stack[-1]과 string의 다음값을 판별하기 위해 next 변수를 1부터 범위 설정
    for next in range(1, len(string)):
        
        # '()'가 만나면 2를 stack에 넣어줌
        if stack[-1] == '(' and string[next] == ')':
            stack.pop()
            stack.append(2)
        
        # '[]'가 만나면 3을 stack에 넣어줌
        elif stack[-1] == '[' and string[next] == ']':
            stack.pop()
            stack.append(3)
        
        # stack[-1]이 괄호가 아니라 숫자인 경우
        elif str(stack[-1]).isdecimal() == True:

            # stack[-1]을 변수 temp로 설정
            temp = stack.pop()
            
            # stack에서 괄호를 만날 때까지 거꾸로 탐색해서 숫자를 더해줌
            while stack and str(stack[-1]).isdecimal() == True:
                temp += stack.pop()
            
            # stack이 비어있으면 temp를 추가하고 string[next]도 추가
            if stack == []:
                stack.append(temp)
                stack.append(string[next])
            
            # '()'안에 temp가 있는 경우이므로 temp에 2를 곱해줌
            elif stack[-1] == '(' and string[next] == ')':
                stack.pop()
                stack.append(temp*2)
            
            # '[]'안에 temp가 있는 경우이므로 temp에 3을 곱해줌
            elif stack[-1] == '[' and string[next] == ']':
                stack.pop()
                stack.append(temp*3)
            
            # temp를 사이에 두는 괄호가 올바른 괄호열이 아닌 경우
            else:
                stack.append(temp)
                stack.append(string[next])

        # stack[-1]이 숫자는 아닌데 string[next]와 올바른 괄호열을 만들지 못하는 경우
        else:   
            stack.append(string[next])


    # stack에 숫자들만 남아있다면 전체 합을 출력하게 하고
    # stack에 숫자가 아닌 괄호가 남아있다면 올바르지 못한 괄호열이므로 0 출력
    try:
        print(sum(stack))
    except:
        print(0)
