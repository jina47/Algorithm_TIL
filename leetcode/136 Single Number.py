from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if i % 2 == 0 and nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]
