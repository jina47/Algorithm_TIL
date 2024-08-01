from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(i, lst):
            result.append(lst)
            for j in range(i+1, len(nums)):
                dfs(j, lst + [nums[j]])

        dfs(-1, [])
        return result


# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         result = []

#         def dfs(index, path):
#             result.append(path)
            
#             for i in range(index, len(nums)):
#                 dfs(i+1, path + [nums[i]])

#         dfs(0, [])
#         return result