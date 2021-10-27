def solution(s):
    ls = [i for i in s]
    stack = []
    for l in ls:
        if len(stack) == 0 or stack[-1] != l:
            stack.append(l)
        elif stack[-1] == l:
            stack.pop()
    if len(stack) == 0:
        return 1
    else:
        return 0