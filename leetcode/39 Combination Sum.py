from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i, result):
            if sum(result) == target:
                results.append(result)
                return
            elif sum(result) < target:
                for j in range(i, len(candidates)):
                    dfs(j, result+[candidates[j]])
        

        results = []
        dfs(0, [])
        return results
    

# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         result = []
        
#         def dfs(csum, index, path):
#             if csum < 0:
#                 return
#             if csum == 0:
#                 result.append(path)
#                 return
            
#             for i in range(index, len(candidates)):
#                 dfs(csum-candidates[i], i, path+[candidates[i]])
        
#         dfs(target, 0, [])
#         return result
        
