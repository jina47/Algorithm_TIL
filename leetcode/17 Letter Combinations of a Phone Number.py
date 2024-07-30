from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz',}
        answer = []

        def dfs(i, char):
            if i == len(digits)-1:
                for alpha in mapping[digits[i]]:
                    answer.append(char+alpha)
                return 
            
            if digits[i] in mapping.keys():
                for alpha in mapping[digits[i]]:
                    dfs(i+1, char + alpha)
            else:
                dfs(i+1, char)

        dfs(0, '')
        return answer
    


# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         def dfs(index, path):
#             if len(path) == len(digits):
#                 result.append(path)
#                 return
            
#             for i in range(index, len(digits)):
#                 for j in dic[digits[i]]:
#                     dfs(i+1, path+j)
        
        
#         if not digits:
#             return []
        
#         dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz',}
#         result = []
#         dfs(0, '')

#         return result