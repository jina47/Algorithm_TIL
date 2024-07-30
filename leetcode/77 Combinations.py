from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1, n+1)]
        result = []

        def dfs(i, lst):
            if len(lst) == k:
                result.append(lst)
                return
            
            for j in range(i, n):
                dfs(j+1, lst+[nums[j]])
        

        dfs(0, [])
        return result
    

# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         results = []

#         def dfs(elements, start: int, k: int):
#             if k == 0:
#                 results.append(elements[:])
#                 return
            
#             for i in range(start, n+1):
#                 elements.append(i)
#                 dfs(elements, i+1, k-1)
#                 elements.pop()
        
#         dfs([], 1, k)
#         return results