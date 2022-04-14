import sys

while True:
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break
    else:
        stack = []
        for s in string:
            if s == '(' or s == '[':
                stack.append(s)
                
            elif s == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s)

            elif s == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(s)

        if stack:
            print('no')
        else:
            print('yes')
