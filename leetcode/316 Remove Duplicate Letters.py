from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        seen = set()

        for char in s:
            counter[char] -= 1
            if not stack:
                stack.append(char)
                seen.add(char)
            
            else:
                if char in seen:
                    continue
                
                # stack[-1]보다 char이 작은데 char 이후의 글자 중에 stack[-1]이 있는 경우 seen과 stack에서 stack[-1] 제거
                while stack and stack[-1] > char and counter[stack[-1]] > 0:
                    seen.remove(stack[-1])
                    stack.pop()

                # char을 방문한 적이 없을 때 stack과 seen에 추가  
                stack.append(char)
                seen.add(char)
            
        return ''.join(stack)
