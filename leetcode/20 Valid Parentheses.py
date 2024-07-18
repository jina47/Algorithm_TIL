class Solution:
    def isValid(self, s:str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        stack = [s[0]]
        for i in range(1, len(s)):
            if len(stack) == 0:
                stack.append(s[i])

            elif s[i] == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif s[i] == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif s[i] == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(s[i])

        if len(stack) == 0:
            return True
        else:
            return False
