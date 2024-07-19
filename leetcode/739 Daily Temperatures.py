from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        stack = [0]
        i = 1
        
        while i < len(temperatures):
            if stack and temperatures[stack[-1]] < temperatures[i]:
                answer[stack[-1]] = i-stack[-1]
                stack.pop()

            else:
                stack.append(i)
                i += 1

        return answer
