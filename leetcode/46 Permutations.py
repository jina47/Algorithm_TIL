from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(lst, visited):
            if len(lst) == len(nums):
                result.append(lst)
                return
            
            for j, num in enumerate(nums):
                if visited[j] == 0:
                    visited[j] = 1
                    dfs(lst + [num], visited)
                    visited[j] = 0

        
        visited = [0 for _ in range(len(nums))]
        result = []

        for i, num in enumerate(nums):
            visited[i] = 1
            dfs([num], visited)
            visited[i] = 0

        return result
    

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         results = []
#         prev_elemenets = []


#         def dfs(elements):
#             if len(elements) == 0:
#                 results.append(prev_elemenets[:])
            
#             for e in elements:
#                 next_elements = elements[:]
#                 next_elements.remove(e)

#                 prev_elemenets.append(e)
#                 dfs(next_elements)
#                 prev_elemenets.pop()
        
    
#         dfs(nums)
#         return results