from typing import List
import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return nums[n//2]
    
# dp
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         counts = collections.defaultdict(int)
#         for num in nums:
#             if counts[num] == 0:
#                 counts[num] = nums.count(num)
            
#             if counts[num] > len(nums) // 2:
#                 return num


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         if not nums:
#             return None
#         if len(nums) == 1:
#             return nums[0]
        
#         half = len(nums) // 2
#         a = self.majorityElement(nums[:half])
#         b = self.majorityElement(nums[half:])

#         return [b, a][nums.count(a) > half]